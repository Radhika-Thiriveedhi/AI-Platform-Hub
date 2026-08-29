"""Platform operations domain service.

Provides deterministic, dependency-free operations used by the application layer for
resource lifecycle management, configuration validation, usage accounting, and
operational reporting.  The service intentionally keeps business rules in Python so
routes can remain thin and easy to test.
"""
from __future__ import annotations

from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from typing import Any, Iterable, Mapping
import hashlib
import math
import re


@dataclass(frozen=True)
class OperationResult:
    """Standard result returned by an operation."""
    ok: bool
    code: str
    message: str
    data: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class ResourceRecord:
    """A managed platform resource."""
    resource_id: str
    resource_type: str
    owner: str
    status: str = "active"
    tags: dict[str, str] = field(default_factory=dict)
    metadata: dict[str, Any] = field(default_factory=dict)
    created_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    updated_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    version: int = 1


class PlatformOperationsService:
    """In-memory domain service for platform resource operations.

    The implementation is deliberately deterministic: callers receive stable error
    codes and predictable dictionaries, making it suitable for API routes, demos,
    integration tests, and local development without a database dependency.
    """

    ALLOWED_TYPES = {
        "model", "dataset", "experiment", "workflow", "integration",
        "prompt", "report", "deployment", "feature", "workspace",
    }
    ALLOWED_STATUSES = {"active", "paused", "archived", "disabled", "draft"}
    NAME_PATTERN = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{1,63}$")

    def __init__(self) -> None:
        self._resources: dict[str, ResourceRecord] = {}
        self._events: list[dict[str, Any]] = []
        self._quotas: dict[str, dict[str, float]] = {}
        self._usage: dict[str, dict[str, float]] = {}

    # ------------------------------------------------------------------
    # Identity and validation helpers
    # ------------------------------------------------------------------
    def _now(self) -> str:
        return datetime.now(timezone.utc).isoformat()

    def _resource_key(self, owner: str, resource_id: str) -> str:
        return f"{owner.strip().lower()}::{resource_id.strip()}"

    def _validate_owner(self, owner: str) -> OperationResult | None:
        if not isinstance(owner, str) or not owner.strip():
            return OperationResult(False, "invalid_owner", "Owner is required")
        if len(owner.strip()) > 128:
            return OperationResult(False, "invalid_owner", "Owner is too long")
        return None

    def _validate_id(self, resource_id: str) -> OperationResult | None:
        if not isinstance(resource_id, str) or not self.NAME_PATTERN.fullmatch(resource_id):
            return OperationResult(False, "invalid_resource_id", "Invalid resource identifier")
        return None

    def _validate_type(self, resource_type: str) -> OperationResult | None:
        if resource_type not in self.ALLOWED_TYPES:
            return OperationResult(False, "invalid_resource_type", "Unsupported resource type")
        return None

    def _validate_status(self, status: str) -> OperationResult | None:
        if status not in self.ALLOWED_STATUSES:
            return OperationResult(False, "invalid_status", "Unsupported resource status")
        return None

    def _validate_tags(self, tags: Mapping[str, Any] | None) -> OperationResult | None:
        if tags is None:
            return None
        if not isinstance(tags, Mapping):
            return OperationResult(False, "invalid_tags", "Tags must be a mapping")
        if len(tags) > 32:
            return OperationResult(False, "invalid_tags", "A resource may have at most 32 tags")
        for key, value in tags.items():
            if not isinstance(key, str) or not key.strip() or len(key) > 64:
                return OperationResult(False, "invalid_tags", "Tag keys must be non-empty strings")
            if not isinstance(value, str) or len(value) > 256:
                return OperationResult(False, "invalid_tags", "Tag values must be strings of at most 256 characters")
        return None

    def _emit(self, owner: str, action: str, resource_id: str, **details: Any) -> None:
        self._events.append({
            "timestamp": self._now(), "owner": owner, "action": action,
            "resource_id": resource_id, "details": details,
        })

    def _record(self, record: ResourceRecord) -> dict[str, Any]:
        value = asdict(record)
        value["tag_count"] = len(record.tags)
        value["metadata_keys"] = sorted(record.metadata)
        return value

    # ------------------------------------------------------------------
    # Resource lifecycle
    # ------------------------------------------------------------------
    def create_resource(self, owner: str, resource_id: str, resource_type: str,
                        tags: Mapping[str, Any] | None = None,
                        metadata: Mapping[str, Any] | None = None) -> OperationResult:
        """Create a resource after validating its identity and attributes."""
        for error in (
            self._validate_owner(owner), self._validate_id(resource_id),
            self._validate_type(resource_type), self._validate_tags(tags),
        ):
            if error:
                return error
        key = self._resource_key(owner, resource_id)
        if key in self._resources:
            return OperationResult(False, "already_exists", "Resource already exists")
        clean_metadata = dict(metadata or {})
        if len(clean_metadata) > 64:
            return OperationResult(False, "invalid_metadata", "Too many metadata fields")
        record = ResourceRecord(
            resource_id=resource_id, resource_type=resource_type, owner=owner.strip(),
            tags={str(k): str(v) for k, v in (tags or {}).items()}, metadata=clean_metadata,
        )
        self._resources[key] = record
        self._emit(owner, "create", resource_id, resource_type=resource_type)
        return OperationResult(True, "created", "Resource created", self._record(record))

    def get_resource(self, owner: str, resource_id: str) -> OperationResult:
        """Return one resource belonging to an owner."""
        error = self._validate_owner(owner) or self._validate_id(resource_id)
        if error:
            return error
        record = self._resources.get(self._resource_key(owner, resource_id))
        if record is None:
            return OperationResult(False, "not_found", "Resource not found")
        return OperationResult(True, "found", "Resource found", self._record(record))

    def update_resource(self, owner: str, resource_id: str,
                        tags: Mapping[str, Any] | None = None,
                        metadata: Mapping[str, Any] | None = None) -> OperationResult:
        """Update mutable resource metadata while preserving its identity."""
        error = self._validate_owner(owner) or self._validate_id(resource_id) or self._validate_tags(tags)
        if error:
            return error
        key = self._resource_key(owner, resource_id)
        record = self._resources.get(key)
        if record is None:
            return OperationResult(False, "not_found", "Resource not found")
        if tags is not None:
            record.tags = {str(k): str(v) for k, v in tags.items()}
        if metadata is not None:
            if len(metadata) > 64:
                return OperationResult(False, "invalid_metadata", "Too many metadata fields")
            record.metadata = dict(metadata)
        record.version += 1
        record.updated_at = self._now()
        self._emit(owner, "update", resource_id, version=record.version)
        return OperationResult(True, "updated", "Resource updated", self._record(record))

    def set_status(self, owner: str, resource_id: str, status: str) -> OperationResult:
        """Move a resource between supported lifecycle states."""
        error = self._validate_owner(owner) or self._validate_id(resource_id) or self._validate_status(status)
        if error:
            return error
        key = self._resource_key(owner, resource_id)
        record = self._resources.get(key)
        if record is None:
            return OperationResult(False, "not_found", "Resource not found")
        if record.status == status:
            return OperationResult(True, "unchanged", "Resource already has requested status", self._record(record))
        previous = record.status
        record.status = status
        record.version += 1
        record.updated_at = self._now()
        self._emit(owner, "status_change", resource_id, previous=previous, current=status)
        return OperationResult(True, "updated", "Resource status updated", self._record(record))

    def archive_resource(self, owner: str, resource_id: str) -> OperationResult:
        """Archive a resource through the common status transition path."""
        return self.set_status(owner, resource_id, "archived")

    def restore_resource(self, owner: str, resource_id: str) -> OperationResult:
        """Restore an archived resource to active state."""
        return self.set_status(owner, resource_id, "active")

    def delete_resource(self, owner: str, resource_id: str) -> OperationResult:
        """Delete a resource and emit an audit event."""
        error = self._validate_owner(owner) or self._validate_id(resource_id)
        if error:
            return error
        key = self._resource_key(owner, resource_id)
        record = self._resources.pop(key, None)
        if record is None:
            return OperationResult(False, "not_found", "Resource not found")
        self._emit(owner, "delete", resource_id, resource_type=record.resource_type)
        return OperationResult(True, "deleted", "Resource deleted", {"resource_id": resource_id})

    def clone_resource(self, owner: str, resource_id: str, new_id: str) -> OperationResult:
        """Clone resource configuration into a new resource identifier."""
        error = self._validate_owner(owner) or self._validate_id(resource_id) or self._validate_id(new_id)
        if error:
            return error
        source = self._resources.get(self._resource_key(owner, resource_id))
        if source is None:
            return OperationResult(False, "not_found", "Source resource not found")
        return self.create_resource(owner, new_id, source.resource_type, source.tags, source.metadata)

    # ------------------------------------------------------------------
    # Search and filtering
    # ------------------------------------------------------------------
    def list_resources(self, owner: str, resource_type: str | None = None,
                       status: str | None = None, tag: str | None = None) -> OperationResult:
        """List resources using optional type, status, and tag filters."""
        error = self._validate_owner(owner)
        if error:
            return error
        if resource_type is not None and (self._validate_type(resource_type) is not None):
            return OperationResult(False, "invalid_resource_type", "Unsupported resource type")
        if status is not None and (self._validate_status(status) is not None):
            return OperationResult(False, "invalid_status", "Unsupported resource status")
        records: list[dict[str, Any]] = []
        for record in self._resources.values():
            if record.owner.lower() != owner.strip().lower():
                continue
            if resource_type and record.resource_type != resource_type:
                continue
            if status and record.status != status:
                continue
            if tag and tag not in record.tags:
                continue
            records.append(self._record(record))
        records.sort(key=lambda item: (item["resource_type"], item["resource_id"]))
        return OperationResult(True, "listed", "Resources listed", {"items": records, "count": len(records)})

    def search_resources(self, owner: str, query: str) -> OperationResult:
        """Search resource identifiers, types, tags, and metadata keys."""
        error = self._validate_owner(owner)
        if error:
            return error
        if not isinstance(query, str) or len(query.strip()) < 2:
            return OperationResult(False, "invalid_query", "Search query must contain at least two characters")
        needle = query.strip().lower()
        matches: list[dict[str, Any]] = []
        for record in self._resources.values():
            if record.owner.lower() != owner.strip().lower():
                continue
            haystack = " ".join([
                record.resource_id, record.resource_type, record.status,
                *record.tags.keys(), *record.tags.values(), *record.metadata.keys(),
            ]).lower()
            if needle in haystack:
                matches.append(self._record(record))
        return OperationResult(True, "searched", "Search completed", {"items": matches, "count": len(matches)})

    def summarize_resources(self, owner: str) -> OperationResult:
        """Produce a compact resource distribution summary."""
        result = self.list_resources(owner)
        if not result.ok:
            return result
        items = result.data["items"]
        by_type: dict[str, int] = {}
        by_status: dict[str, int] = {}
        for item in items:
            by_type[item["resource_type"]] = by_type.get(item["resource_type"], 0) + 1
            by_status[item["status"]] = by_status.get(item["status"], 0) + 1
        return OperationResult(True, "summarized", "Resource summary created", {
            "total": len(items), "by_type": by_type, "by_status": by_status,
        })

    # ------------------------------------------------------------------
    # Quota and usage accounting
    # ------------------------------------------------------------------
    def configure_quota(self, owner: str, metric: str, limit: float) -> OperationResult:
        """Configure a non-negative usage quota for an owner."""
        error = self._validate_owner(owner)
        if error:
            return error
        if not isinstance(metric, str) or not re.fullmatch(r"[A-Za-z][A-Za-z0-9_.-]{1,63}", metric):
            return OperationResult(False, "invalid_metric", "Invalid quota metric")
        if not isinstance(limit, (int, float)) or not math.isfinite(float(limit)) or limit < 0:
            return OperationResult(False, "invalid_limit", "Quota limit must be finite and non-negative")
        self._quotas.setdefault(owner.strip().lower(), {})[metric] = float(limit)
        self._usage.setdefault(owner.strip().lower(), {}).setdefault(metric, 0.0)
        self._emit(owner, "quota_configure", metric, limit=float(limit))
        return OperationResult(True, "configured", "Quota configured", {"metric": metric, "limit": float(limit)})

    def record_usage(self, owner: str, metric: str, amount: float) -> OperationResult:
        """Record usage and report whether the resulting value remains within quota."""
        error = self._validate_owner(owner)
        if error:
            return error
        if not isinstance(metric, str) or not metric.strip():
            return OperationResult(False, "invalid_metric", "Usage metric is required")
        if not isinstance(amount, (int, float)) or not math.isfinite(float(amount)) or amount < 0:
            return OperationResult(False, "invalid_amount", "Usage amount must be finite and non-negative")
        key = owner.strip().lower()
        current = self._usage.setdefault(key, {}).get(metric, 0.0)
        new_value = current + float(amount)
        limit = self._quotas.setdefault(key, {}).get(metric)
        if limit is not None and new_value > limit:
            return OperationResult(False, "quota_exceeded", "Usage would exceed quota", {
                "metric": metric, "current": current, "requested": float(amount), "limit": limit,
            })
        self._usage[key][metric] = new_value
        self._emit(owner, "usage_record", metric, amount=float(amount), total=new_value)
        return OperationResult(True, "recorded", "Usage recorded", {
            "metric": metric, "amount": float(amount), "total": new_value, "limit": limit,
        })

    def get_usage(self, owner: str) -> OperationResult:
        """Return usage, quota, remaining capacity, and utilization."""
        error = self._validate_owner(owner)
        if error:
            return error
        key = owner.strip().lower()
        usage = self._usage.get(key, {})
        quotas = self._quotas.get(key, {})
        rows: dict[str, dict[str, float | None]] = {}
        for metric in sorted(set(usage) | set(quotas)):
            value = float(usage.get(metric, 0.0))
            limit = quotas.get(metric)
            remaining = None if limit is None else max(0.0, limit - value)
            utilization = None if limit in (None, 0) else value / limit
            rows[metric] = {"usage": value, "limit": limit, "remaining": remaining, "utilization": utilization}
        return OperationResult(True, "usage", "Usage returned", {"metrics": rows})

    def reset_usage(self, owner: str, metric: str | None = None) -> OperationResult:
        """Reset all usage or one usage metric for an owner."""
        error = self._validate_owner(owner)
        if error:
            return error
        key = owner.strip().lower()
        if metric is None:
            self._usage[key] = {}
        else:
            self._usage.setdefault(key, {}).pop(metric, None)
        self._emit(owner, "usage_reset", metric or "all")
        return OperationResult(True, "reset", "Usage reset", {"metric": metric})

    # ------------------------------------------------------------------
    # Configuration fingerprints and health checks
    # ------------------------------------------------------------------
    def resource_fingerprint(self, owner: str, resource_id: str) -> OperationResult:
        """Return a stable SHA-256 fingerprint of resource configuration."""
        result = self.get_resource(owner, resource_id)
        if not result.ok:
            return result
        record = result.data
        canonical = "|".join([
            str(record["resource_id"]), str(record["resource_type"]), str(record["owner"]),
            str(record["status"]), repr(sorted(record["tags"].items())),
            repr(sorted(record["metadata"].items())), str(record["version"]),
        ])
        digest = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
        return OperationResult(True, "fingerprint", "Fingerprint calculated", {"sha256": digest})

    def health_check(self, owner: str) -> OperationResult:
        """Run inexpensive consistency checks over an owner's resources."""
        error = self._validate_owner(owner)
        if error:
            return error
        key = owner.strip().lower()
        problems: list[str] = []
        for record in self._resources.values():
            if record.owner.lower() != key:
                continue
            if record.status not in self.ALLOWED_STATUSES:
                problems.append(f"{record.resource_id}:invalid_status")
            if record.version < 1:
                problems.append(f"{record.resource_id}:invalid_version")
            if len(record.tags) > 32:
                problems.append(f"{record.resource_id}:too_many_tags")
        healthy = not problems
        return OperationResult(healthy, "healthy" if healthy else "degraded",
                               "Resource health check completed", {
                                   "healthy": healthy, "problems": problems,
                               })

    def event_log(self, owner: str, limit: int = 100) -> OperationResult:
        """Return the most recent operational events for an owner."""
        error = self._validate_owner(owner)
        if error:
            return error
        if not isinstance(limit, int) or limit < 1 or limit > 1000:
            return OperationResult(False, "invalid_limit", "Event limit must be between 1 and 1000")
        events = [event for event in self._events if event["owner"].lower() == owner.strip().lower()]
        return OperationResult(True, "events", "Event log returned", {"items": events[-limit:]})


# ----------------------------------------------------------------------
# Deterministic helper operations kept outside the service for reuse by
# routes and other services. Each helper validates its inputs and returns
# a small structured result rather than raising application-level errors.
# ----------------------------------------------------------------------

def normalize_resource_tags(tags: Mapping[str, Any] | None) -> dict[str, str]:
    """Normalize tag keys and values for consistent filtering."""
    if not tags:
        return {}
    normalized: dict[str, str] = {}
    for key, value in tags.items():
        clean_key = str(key).strip().lower().replace(" ", "_")
        clean_value = str(value).strip()
        if clean_key:
            normalized[clean_key] = clean_value
    return dict(sorted(normalized.items()))


def calculate_utilization(used: float, limit: float | None) -> float | None:
    """Calculate utilization safely, returning None when no limit exists."""
    if limit is None:
        return None
    if limit <= 0:
        return 1.0 if used > 0 else 0.0
    return max(0.0, float(used)) / float(limit)


def paginate_items(items: Iterable[Any], page: int = 1, page_size: int = 25) -> dict[str, Any]:
    """Return deterministic pagination metadata for an iterable."""
    values = list(items)
    page = max(1, int(page))
    page_size = min(200, max(1, int(page_size)))
    total = len(values)
    pages = max(1, math.ceil(total / page_size))
    start = (page - 1) * page_size
    return {
        "items": values[start:start + page_size], "page": page,
        "page_size": page_size, "pages": pages, "total": total,
        "has_next": page < pages, "has_previous": page > 1,
    }
