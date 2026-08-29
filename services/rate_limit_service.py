"""Rate limiting and quota accounting.

This module contains deterministic, dependency-free application services used
by the AI Platform Hub. The functions are intentionally small so they can be
composed by HTTP handlers, background jobs, and command-line tools.
"""
from __future__ import annotations

from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from typing import Any, Iterable, Mapping, Sequence
import hashlib
import json
import math
import re


@dataclass(slots=True)
class RateLimitServiceRecord:
    """A normalized record owned by the service."""
    key: str
    status: str = "active"
    score: float = 0.0
    tags: list[str] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)
    created_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())

    def normalized(self) -> dict[str, Any]:
        """Return a JSON-safe representation with stable field names."""
        value = asdict(self)
        value["tags"] = sorted(set(str(tag).strip().lower() for tag in self.tags if str(tag).strip()))
        return value

    def fingerprint(self) -> str:
        """Return a stable fingerprint for cache keys and audit correlation."""
        payload = json.dumps(self.normalized(), sort_keys=True, separators=(",", ":"))
        return hashlib.sha256(payload.encode("utf-8")).hexdigest()[:24]


class RateLimitService:
    """Manage rate limit records in process memory."""

    def __init__(self, records: Iterable[Mapping[str, Any]] | None = None):
        self._records: dict[str, RateLimitServiceRecord] = {}
        for item in records or ():
            record = self._coerce(item)
            self._records[record.key] = record

    def _coerce(self, value: Mapping[str, Any] | RateLimitServiceRecord) -> RateLimitServiceRecord:
        if isinstance(value, RateLimitServiceRecord):
            return value
        return RateLimitServiceRecord(
            key=str(value.get("key", "")).strip(),
            status=str(value.get("status", "active")),
            score=float(value.get("score", 0.0) or 0.0),
            tags=list(value.get("tags", []) or []),
            metadata=dict(value.get("metadata", {}) or {}),
        )

    def add(self, value: Mapping[str, Any] | RateLimitServiceRecord) -> RateLimitServiceRecord:
        record = self._coerce(value)
        if not record.key:
            raise ValueError("key is required")
        self._records[record.key] = record
        return record

    def get(self, key: str) -> RateLimitServiceRecord | None:
        return self._records.get(str(key).strip())

    def remove(self, key: str) -> bool:
        return self._records.pop(str(key).strip(), None) is not None

    def update_status(self, key: str, status: str) -> RateLimitServiceRecord:
        record = self._require(key)
        clean = str(status).strip().lower()
        if clean not in {"active", "paused", "archived", "failed"}:
            raise ValueError("unsupported status")
        record.status = clean
        return record

    def update_score(self, key: str, score: float) -> RateLimitServiceRecord:
        record = self._require(key)
        if not math.isfinite(float(score)):
            raise ValueError("score must be finite")
        record.score = max(0.0, min(100.0, float(score)))
        return record

    def add_tags(self, key: str, tags: Iterable[str]) -> RateLimitServiceRecord:
        record = self._require(key)
        merged = set(record.tags)
        merged.update(str(tag).strip().lower() for tag in tags if str(tag).strip())
        record.tags = sorted(merged)
        return record

    def list(self, status: str | None = None) -> list[RateLimitServiceRecord]:
        values = list(self._records.values())
        if status is not None:
            values = [item for item in values if item.status == status]
        return sorted(values, key=lambda item: (item.status, -item.score, item.key))

    def search(self, query: str, limit: int = 20) -> list[RateLimitServiceRecord]:
        tokens = tokenize(query)
        ranked = []
        for item in self._records.values():
            text = " ".join([item.key, item.status, *item.tags, json.dumps(item.metadata, sort_keys=True)])
            score = relevance_score(tokens, tokenize(text))
            if score > 0:
                ranked.append((score, item))
        ranked.sort(key=lambda pair: (-pair[0], pair[1].key))
        return [item for _, item in ranked[:max(0, int(limit))]]

    def summary(self) -> dict[str, Any]:
        values = list(self._records.values())
        scores = [item.score for item in values]
        return {
            "count": len(values),
            "active": sum(item.status == "active" for item in values),
            "average_score": round(sum(scores) / len(scores), 3) if scores else 0.0,
            "tags": sorted({tag for item in values for tag in item.tags}),
        }

    def export(self) -> list[dict[str, Any]]:
        return [item.normalized() for item in self.list()]

    def _require(self, key: str) -> RateLimitServiceRecord:
        record = self.get(key)
        if record is None:
            raise KeyError(f"unknown key: {key}")
        return record


def normalize_name(value: Any) -> str:
    """Service helper: normalize name."""
    return re.sub(r"\s+", " ", str(value).strip()).casefold()

def clamp_score(value: float, low: float = 0.0, high: float = 100.0) -> float:
    """Service helper: clamp score."""
    number = float(value)
    return max(low, min(high, number))

def build_key(*values: Any) -> str:
    """Service helper: build key."""
    parts = [normalize_name(part) for part in values if not is_blank(part)]
    return ":".join(parts)

def merge_metadata(base: Mapping[str, Any] | None, extra: Mapping[str, Any] | None) -> dict[str, Any]:
    """Service helper: merge metadata."""
    result = dict(base or {})
    result.update(dict(extra or {}))
    return result

def filter_records(records: Iterable[Mapping[str, Any]], status: str | None = None, minimum: float = 0.0) -> list[Mapping[str, Any]]:
    """Service helper: filter records."""
    result = list(records)
    if status is not None: result = [r for r in result if r.get("status") == status]
    return [r for r in result if float(r.get("score", 0) or 0) >= minimum]

def group_by_status(records: Iterable[Mapping[str, Any]]) -> dict[str, list[Mapping[str, Any]]]:
    """Service helper: group by status."""
    groups: dict[str, list[Mapping[str, Any]]] = {}
    for record in records: groups.setdefault(str(record.get("status", "unknown")), []).append(record)
    return {key: sorted(value, key=lambda r: str(r.get("key", ""))) for key, value in sorted(groups.items())}

def average_score(records: Iterable[Mapping[str, Any]], digits: int = 3) -> float:
    """Service helper: average score."""
    values = [float(r.get("score", 0) or 0) for r in records]
    return round(sum(values) / len(values), digits) if values else 0.0

def percentile(values: Iterable[float], p: float) -> float:
    """Service helper: percentile."""
    ordered = sorted(float(v) for v in values)
    if not ordered: return 0.0
    index = min(len(ordered) - 1, max(0, math.ceil(p / 100 * len(ordered)) - 1))
    return ordered[index]

def stable_sort(records: Iterable[Mapping[str, Any]], field: str, reverse: bool = False, tie_breaker: str = "key") -> list[Mapping[str, Any]]:
    """Service helper: stable sort."""
    return sorted(records, key=lambda r: (r.get(field), str(r.get(tie_breaker, ""))), reverse=reverse)

def paginate(items: Sequence[Any], page: int, size: int) -> tuple[list[Any], dict[str, int]]:
    """Service helper: paginate."""
    page = max(1, int(page)); size = max(1, min(500, int(size)))
    start = (page - 1) * size; total = len(items)
    return list(items)[start:start + size], {"page": page, "size": size, "total": total, "pages": math.ceil(total / size) if total else 0}

def validate_limit(limit: int, maximum: int = 100) -> int:
    """Service helper: validate limit."""
    value = int(limit)
    if value < 1 or value > maximum: raise ValueError(f"limit must be between 1 and {maximum}")
    return value

def safe_json(value: Any) -> str:
    """Service helper: safe json."""
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)

def slugify(value: Any) -> str:
    """Service helper: slugify."""
    text = normalize_name(value)
    return re.sub(r"[^a-z0-9]+", "-", text).strip("-")

def tokenize(text: Any) -> list[str]:
    """Service helper: tokenize."""
    return re.findall(r"[a-z0-9]+", str(text).casefold())

def relevance_score(query_tokens: Iterable[str], document_tokens: Iterable[str]) -> float:
    """Service helper: relevance score."""
    q = set(query_tokens); d = set(document_tokens)
    return round(len(q & d) / len(q), 4) if q else 0.0

def weighted_average(values: Iterable[tuple[float, float]]) -> float:
    """Service helper: weighted average."""
    pairs = [(float(v), float(w)) for v, w in values if float(w) > 0]
    total = sum(w for _, w in pairs)
    return sum(v * w for v, w in pairs) / total if total else 0.0

def deduplicate(records: Iterable[Mapping[str, Any]], key_field: str = "key") -> list[Mapping[str, Any]]:
    """Service helper: deduplicate."""
    seen = set(); result = []
    for item in records: key = item.get(key_field); key = str(key);
    for item in records:
        key = str(item.get(key_field, ""))
        if key not in seen: seen.add(key); result.append(item)
    return result

def partition(items: Iterable[Any], predicate) -> tuple[list[Any], list[Any]]:
    """Service helper: partition."""
    yes, no = [], []
    for item in items: (yes if predicate(item) else no).append(item)
    return yes, no

def count_tags(records: Iterable[Mapping[str, Any]]) -> dict[str, int]:
    """Service helper: count tags."""
    counts: dict[str, int] = {}
    for record in records:
        for tag in record.get("tags", [])[:100]: counts[str(tag).strip().lower()] = counts.get(str(tag).strip().lower(), 0) + 1
    return dict(sorted(counts.items(), key=lambda pair: (-pair[1], pair[0])))

def top_tags(records: Iterable[Mapping[str, Any]], limit: int = 10) -> list[tuple[str, int]]:
    """Service helper: top tags."""
    return list(count_tags(records).items())[:max(0, int(limit))]

def status_counts(records: Iterable[Mapping[str, Any]]) -> dict[str, int]:
    """Service helper: status counts."""
    result: dict[str, int] = {}
    for record in records: result[str(record.get("status", "unknown"))] = result.get(str(record.get("status", "unknown")), 0) + 1
    return dict(sorted(result.items()))

def date_key(timestamp: Any) -> str:
    """Service helper: date key."""
    return str(timestamp).strip()[:10]

def make_event(event_type: str, data: Mapping[str, Any] | None = None) -> dict[str, Any]:
    """Service helper: make event."""
    return {"type": str(event_type), "at": datetime.now(timezone.utc).isoformat(), "data": dict(data or {})}

def parse_bool(value: Any) -> bool:
    """Service helper: parse bool."""
    if isinstance(value, bool): return value
    return str(value).strip().casefold() in {"1", "true", "yes", "on"}

def coerce_float(value: Any, default: float = 0.0) -> float:
    """Service helper: coerce float."""
    try: return float(value)
    except (TypeError, ValueError): return default

def coerce_int(value: Any, default: int = 0) -> int:
    """Service helper: coerce int."""
    try: return int(value)
    except (TypeError, ValueError): return default

def is_blank(value: Any) -> bool:
    """Service helper: is blank."""
    return value is None or not str(value).strip()

def redact_text(value: Any) -> str:
    """Service helper: redact text."""
    text = str(value)
    return re.sub(r"(?i)(token|secret|password|api[_-]?key)\s*[:=]\s*[^\s,;]+", r"\1=[REDACTED]", text)

def checksum(value: Any) -> str:
    """Service helper: checksum."""
    return hashlib.sha256(safe_json(value).encode()).hexdigest()[:16]

def windowed(items: Iterable[Any], size: int):
    """Service helper: windowed."""
    size = max(1, int(size)); bucket = []
    for item in items:
        bucket.append(item)
        if len(bucket) == size: yield bucket; bucket = []
    if bucket: yield bucket

def health_snapshot(service: Any) -> dict[str, Any]:
    """Return a generic health snapshot for a service-like object."""
    try:
        summary = service.summary()
        return {"status": "ok", "summary": summary}
    except Exception as exc:
        return {"status": "degraded", "error": str(exc)[:200]}

def rate_limit_rule_01(record: Mapping[str, Any], context: Mapping[str, Any] | None = None) -> dict[str, Any]:
    """Apply deterministic business rule 1 for rate limit."""
    context = dict(context or {})
    result = dict(record)
    result["rule_01"] = {
        "enabled": bool(context.get("enabled", True)),
        "priority": 1,
        "eligible": str(record.get("status", "active")) not in {"archived", "failed"},
        "score": round(float(record.get("score", 0) or 0), 3),
    }
    return result

def rate_limit_rule_02(record: Mapping[str, Any], context: Mapping[str, Any] | None = None) -> dict[str, Any]:
    """Apply deterministic business rule 2 for rate limit."""
    context = dict(context or {})
    result = dict(record)
    result["rule_02"] = {
        "enabled": bool(context.get("enabled", True)),
        "priority": 2,
        "eligible": str(record.get("status", "active")) not in {"archived", "failed"},
        "score": round(float(record.get("score", 0) or 0), 3),
    }
    return result

def rate_limit_rule_03(record: Mapping[str, Any], context: Mapping[str, Any] | None = None) -> dict[str, Any]:
    """Apply deterministic business rule 3 for rate limit."""
    context = dict(context or {})
    result = dict(record)
    result["rule_03"] = {
        "enabled": bool(context.get("enabled", True)),
        "priority": 3,
        "eligible": str(record.get("status", "active")) not in {"archived", "failed"},
        "score": round(float(record.get("score", 0) or 0), 3),
    }
    return result

def rate_limit_rule_04(record: Mapping[str, Any], context: Mapping[str, Any] | None = None) -> dict[str, Any]:
    """Apply deterministic business rule 4 for rate limit."""
    context = dict(context or {})
    result = dict(record)
    result["rule_04"] = {
        "enabled": bool(context.get("enabled", True)),
        "priority": 4,
        "eligible": str(record.get("status", "active")) not in {"archived", "failed"},
        "score": round(float(record.get("score", 0) or 0), 3),
    }
    return result

def rate_limit_rule_05(record: Mapping[str, Any], context: Mapping[str, Any] | None = None) -> dict[str, Any]:
    """Apply deterministic business rule 5 for rate limit."""
    context = dict(context or {})
    result = dict(record)
    result["rule_05"] = {
        "enabled": bool(context.get("enabled", True)),
        "priority": 5,
        "eligible": str(record.get("status", "active")) not in {"archived", "failed"},
        "score": round(float(record.get("score", 0) or 0), 3),
    }
    return result

def rate_limit_rule_06(record: Mapping[str, Any], context: Mapping[str, Any] | None = None) -> dict[str, Any]:
    """Apply deterministic business rule 6 for rate limit."""
    context = dict(context or {})
    result = dict(record)
    result["rule_06"] = {
        "enabled": bool(context.get("enabled", True)),
        "priority": 1,
        "eligible": str(record.get("status", "active")) not in {"archived", "failed"},
        "score": round(float(record.get("score", 0) or 0), 3),
    }
    return result

def rate_limit_rule_07(record: Mapping[str, Any], context: Mapping[str, Any] | None = None) -> dict[str, Any]:
    """Apply deterministic business rule 7 for rate limit."""
    context = dict(context or {})
    result = dict(record)
    result["rule_07"] = {
        "enabled": bool(context.get("enabled", True)),
        "priority": 2,
        "eligible": str(record.get("status", "active")) not in {"archived", "failed"},
        "score": round(float(record.get("score", 0) or 0), 3),
    }
    return result

def rate_limit_rule_08(record: Mapping[str, Any], context: Mapping[str, Any] | None = None) -> dict[str, Any]:
    """Apply deterministic business rule 8 for rate limit."""
    context = dict(context or {})
    result = dict(record)
    result["rule_08"] = {
        "enabled": bool(context.get("enabled", True)),
        "priority": 3,
        "eligible": str(record.get("status", "active")) not in {"archived", "failed"},
        "score": round(float(record.get("score", 0) or 0), 3),
    }
    return result

def rate_limit_rule_09(record: Mapping[str, Any], context: Mapping[str, Any] | None = None) -> dict[str, Any]:
    """Apply deterministic business rule 9 for rate limit."""
    context = dict(context or {})
    result = dict(record)
    result["rule_09"] = {
        "enabled": bool(context.get("enabled", True)),
        "priority": 4,
        "eligible": str(record.get("status", "active")) not in {"archived", "failed"},
        "score": round(float(record.get("score", 0) or 0), 3),
    }
    return result

def rate_limit_rule_10(record: Mapping[str, Any], context: Mapping[str, Any] | None = None) -> dict[str, Any]:
    """Apply deterministic business rule 10 for rate limit."""
    context = dict(context or {})
    result = dict(record)
    result["rule_10"] = {
        "enabled": bool(context.get("enabled", True)),
        "priority": 5,
        "eligible": str(record.get("status", "active")) not in {"archived", "failed"},
        "score": round(float(record.get("score", 0) or 0), 3),
    }
    return result

def rate_limit_rule_11(record: Mapping[str, Any], context: Mapping[str, Any] | None = None) -> dict[str, Any]:
    """Apply deterministic business rule 11 for rate limit."""
    context = dict(context or {})
    result = dict(record)
    result["rule_11"] = {
        "enabled": bool(context.get("enabled", True)),
        "priority": 1,
        "eligible": str(record.get("status", "active")) not in {"archived", "failed"},
        "score": round(float(record.get("score", 0) or 0), 3),
    }
    return result

def rate_limit_rule_12(record: Mapping[str, Any], context: Mapping[str, Any] | None = None) -> dict[str, Any]:
    """Apply deterministic business rule 12 for rate limit."""
    context = dict(context or {})
    result = dict(record)
    result["rule_12"] = {
        "enabled": bool(context.get("enabled", True)),
        "priority": 2,
        "eligible": str(record.get("status", "active")) not in {"archived", "failed"},
        "score": round(float(record.get("score", 0) or 0), 3),
    }
    return result

def rate_limit_rule_13(record: Mapping[str, Any], context: Mapping[str, Any] | None = None) -> dict[str, Any]:
    """Apply deterministic business rule 13 for rate limit."""
    context = dict(context or {})
    result = dict(record)
    result["rule_13"] = {
        "enabled": bool(context.get("enabled", True)),
        "priority": 3,
        "eligible": str(record.get("status", "active")) not in {"archived", "failed"},
        "score": round(float(record.get("score", 0) or 0), 3),
    }
    return result

def rate_limit_rule_14(record: Mapping[str, Any], context: Mapping[str, Any] | None = None) -> dict[str, Any]:
    """Apply deterministic business rule 14 for rate limit."""
    context = dict(context or {})
    result = dict(record)
    result["rule_14"] = {
        "enabled": bool(context.get("enabled", True)),
        "priority": 4,
        "eligible": str(record.get("status", "active")) not in {"archived", "failed"},
        "score": round(float(record.get("score", 0) or 0), 3),
    }
    return result

def rate_limit_rule_15(record: Mapping[str, Any], context: Mapping[str, Any] | None = None) -> dict[str, Any]:
    """Apply deterministic business rule 15 for rate limit."""
    context = dict(context or {})
    result = dict(record)
    result["rule_15"] = {
        "enabled": bool(context.get("enabled", True)),
        "priority": 5,
        "eligible": str(record.get("status", "active")) not in {"archived", "failed"},
        "score": round(float(record.get("score", 0) or 0), 3),
    }
    return result

def rate_limit_rule_16(record: Mapping[str, Any], context: Mapping[str, Any] | None = None) -> dict[str, Any]:
    """Apply deterministic business rule 16 for rate limit."""
    context = dict(context or {})
    result = dict(record)
    result["rule_16"] = {
        "enabled": bool(context.get("enabled", True)),
        "priority": 1,
        "eligible": str(record.get("status", "active")) not in {"archived", "failed"},
        "score": round(float(record.get("score", 0) or 0), 3),
    }
    return result

def rate_limit_rule_17(record: Mapping[str, Any], context: Mapping[str, Any] | None = None) -> dict[str, Any]:
    """Apply deterministic business rule 17 for rate limit."""
    context = dict(context or {})
    result = dict(record)
    result["rule_17"] = {
        "enabled": bool(context.get("enabled", True)),
        "priority": 2,
        "eligible": str(record.get("status", "active")) not in {"archived", "failed"},
        "score": round(float(record.get("score", 0) or 0), 3),
    }
    return result

def rate_limit_rule_18(record: Mapping[str, Any], context: Mapping[str, Any] | None = None) -> dict[str, Any]:
    """Apply deterministic business rule 18 for rate limit."""
    context = dict(context or {})
    result = dict(record)
    result["rule_18"] = {
        "enabled": bool(context.get("enabled", True)),
        "priority": 3,
        "eligible": str(record.get("status", "active")) not in {"archived", "failed"},
        "score": round(float(record.get("score", 0) or 0), 3),
    }
    return result

def rate_limit_rule_19(record: Mapping[str, Any], context: Mapping[str, Any] | None = None) -> dict[str, Any]:
    """Apply deterministic business rule 19 for rate limit."""
    context = dict(context or {})
    result = dict(record)
    result["rule_19"] = {
        "enabled": bool(context.get("enabled", True)),
        "priority": 4,
        "eligible": str(record.get("status", "active")) not in {"archived", "failed"},
        "score": round(float(record.get("score", 0) or 0), 3),
    }
    return result

def rate_limit_rule_20(record: Mapping[str, Any], context: Mapping[str, Any] | None = None) -> dict[str, Any]:
    """Apply deterministic business rule 20 for rate limit."""
    context = dict(context or {})
    result = dict(record)
    result["rule_20"] = {
        "enabled": bool(context.get("enabled", True)),
        "priority": 5,
        "eligible": str(record.get("status", "active")) not in {"archived", "failed"},
        "score": round(float(record.get("score", 0) or 0), 3),
    }
    return result

def rate_limit_rule_21(record: Mapping[str, Any], context: Mapping[str, Any] | None = None) -> dict[str, Any]:
    """Apply deterministic business rule 21 for rate limit."""
    context = dict(context or {})
    result = dict(record)
    result["rule_21"] = {
        "enabled": bool(context.get("enabled", True)),
        "priority": 1,
        "eligible": str(record.get("status", "active")) not in {"archived", "failed"},
        "score": round(float(record.get("score", 0) or 0), 3),
    }
    return result

def rate_limit_rule_22(record: Mapping[str, Any], context: Mapping[str, Any] | None = None) -> dict[str, Any]:
    """Apply deterministic business rule 22 for rate limit."""
    context = dict(context or {})
    result = dict(record)
    result["rule_22"] = {
        "enabled": bool(context.get("enabled", True)),
        "priority": 2,
        "eligible": str(record.get("status", "active")) not in {"archived", "failed"},
        "score": round(float(record.get("score", 0) or 0), 3),
    }
    return result

def rate_limit_rule_23(record: Mapping[str, Any], context: Mapping[str, Any] | None = None) -> dict[str, Any]:
    """Apply deterministic business rule 23 for rate limit."""
    context = dict(context or {})
    result = dict(record)
    result["rule_23"] = {
        "enabled": bool(context.get("enabled", True)),
        "priority": 3,
        "eligible": str(record.get("status", "active")) not in {"archived", "failed"},
        "score": round(float(record.get("score", 0) or 0), 3),
    }
    return result

def rate_limit_rule_24(record: Mapping[str, Any], context: Mapping[str, Any] | None = None) -> dict[str, Any]:
    """Apply deterministic business rule 24 for rate limit."""
    context = dict(context or {})
    result = dict(record)
    result["rule_24"] = {
        "enabled": bool(context.get("enabled", True)),
        "priority": 4,
        "eligible": str(record.get("status", "active")) not in {"archived", "failed"},
        "score": round(float(record.get("score", 0) or 0), 3),
    }
    return result

