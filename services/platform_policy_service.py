"""Policy and governance operations for the AI Platform Hub.

This module centralizes small, deterministic policy decisions used by API routes and
service orchestration. It has no external dependencies and is safe for local demos.
"""
from __future__ import annotations

from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from typing import Any, Iterable, Mapping
import re

@dataclass
class PolicyDecision:
    allowed: bool
    code: str
    reason: str
    metadata: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

class PlatformPolicyService:
    """Evaluate access, payload, naming, lifecycle, and operational policies."""
    MAX_TEXT = 10000
    MAX_BATCH = 100
    RESERVED_NAMES = {"admin", "root", "system", "health", "status"}
    SAFE_NAME = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.-]{1,63}$")

    def __init__(self) -> None:
        self._decisions: list[dict[str, Any]] = []

    def _decision(self, allowed: bool, code: str, reason: str, **metadata: Any) -> PolicyDecision:
        result = PolicyDecision(allowed, code, reason, metadata)
        self._decisions.append({"time": datetime.now(timezone.utc).isoformat(), **result.to_dict()})
        return result

    def _text(self, value: Any, field: str) -> PolicyDecision | None:
        if not isinstance(value, str) or not value.strip():
            return self._decision(False, "invalid_text", f"{field} is required")
        if len(value) > self.MAX_TEXT:
            return self._decision(False, "text_too_long", f"{field} exceeds the maximum length")
        return None
    def allow_chat_request(self, payload: Mapping[str, Any]) -> PolicyDecision:
        """Validate a chat request.."""
        if not isinstance(payload, Mapping):
            return self._decision(False, "invalid_payload", "Chat payload must be an object")
        messages = payload.get("messages")
        if not isinstance(messages, list) or not messages:
            return self._decision(False, "missing_messages", "At least one message is required")
        if len(messages) > self.MAX_BATCH:
            return self._decision(False, "batch_too_large", "Too many messages")
        for message in messages:
            if not isinstance(message, Mapping) or not isinstance(message.get("content"), str):
                return self._decision(False, "invalid_message", "Every message requires text content")
            if len(message["content"]) > self.MAX_TEXT:
                return self._decision(False, "message_too_long", "Message exceeds the maximum length")
        return self._decision(True, "accepted", "Chat request accepted", message_count=len(messages))

    def allow_batch_request(self, items: Iterable[Any]) -> PolicyDecision:
        """Validate a batch request.."""
        if not isinstance(items, Iterable) or isinstance(items, (str, bytes, Mapping)):
            return self._decision(False, "invalid_batch", "Batch must be an iterable of items")
        values = list(items)
        if not values:
            return self._decision(False, "empty_batch", "Batch cannot be empty")
        if len(values) > self.MAX_BATCH:
            return self._decision(False, "batch_too_large", "Batch exceeds the maximum size")
        return self._decision(True, "accepted", "Batch request accepted", item_count=len(values))

    def allow_model_name(self, name: Any) -> PolicyDecision:
        """Validate a model name.."""
        if not isinstance(name, str):
            return self._decision(False, "invalid_value", "Value has an invalid type")
        if not (bool(self.SAFE_NAME.fullmatch(name)) and name.lower() not in self.RESERVED_NAMES):
            return self._decision(False, "policy_denied", "Value does not satisfy platform policy")
        return self._decision(True, "accepted", "Model name accepted", value=name)

    def allow_dataset_name(self, name: Any) -> PolicyDecision:
        """Validate a dataset name.."""
        if not isinstance(name, str):
            return self._decision(False, "invalid_value", "Value has an invalid type")
        if not (bool(self.SAFE_NAME.fullmatch(name))):
            return self._decision(False, "policy_denied", "Value does not satisfy platform policy")
        return self._decision(True, "accepted", "Dataset name accepted", value=name)

    def allow_workspace_name(self, name: Any) -> PolicyDecision:
        """Validate a workspace name.."""
        if not isinstance(name, str):
            return self._decision(False, "invalid_value", "Value has an invalid type")
        if not (bool(self.SAFE_NAME.fullmatch(name))):
            return self._decision(False, "policy_denied", "Value does not satisfy platform policy")
        return self._decision(True, "accepted", "Workspace name accepted", value=name)

    def allow_prompt(self, prompt: Any) -> PolicyDecision:
        """Validate a prompt payload.."""
        if not isinstance(prompt, str):
            return self._decision(False, "invalid_value", "Value has an invalid type")
        if not (len(prompt.strip()) <= self.MAX_TEXT):
            return self._decision(False, "policy_denied", "Value does not satisfy platform policy")
        return self._decision(True, "accepted", "Prompt accepted", value=prompt)

    def allow_description(self, description: Any) -> PolicyDecision:
        """Validate a description.."""
        if not isinstance(description, str):
            return self._decision(False, "invalid_value", "Value has an invalid type")
        if not (len(description.strip()) <= self.MAX_TEXT):
            return self._decision(False, "policy_denied", "Value does not satisfy platform policy")
        return self._decision(True, "accepted", "Description accepted", value=description)

    def allow_tag_count(self, count: Any) -> PolicyDecision:
        """Validate tag count.."""
        if not isinstance(count, int):
            return self._decision(False, "invalid_value", "Value has an invalid type")
        if not (0 <= count <= 32):
            return self._decision(False, "policy_denied", "Value does not satisfy platform policy")
        return self._decision(True, "accepted", "Tag count accepted", value=count)

    def allow_page_size(self, size: Any) -> PolicyDecision:
        """Validate pagination size.."""
        if not isinstance(size, int):
            return self._decision(False, "invalid_value", "Value has an invalid type")
        if not (1 <= size <= 200):
            return self._decision(False, "policy_denied", "Value does not satisfy platform policy")
        return self._decision(True, "accepted", "Page size accepted", value=size)

    def allow_timeout(self, seconds: Any) -> PolicyDecision:
        """Validate an operation timeout.."""
        if not isinstance(seconds, int):
            return self._decision(False, "invalid_value", "Value has an invalid type")
        if not (1 <= seconds <= 300):
            return self._decision(False, "policy_denied", "Value does not satisfy platform policy")
        return self._decision(True, "accepted", "Timeout accepted", value=seconds)

    def allow_retry_count(self, count: Any) -> PolicyDecision:
        """Validate retry count.."""
        if not isinstance(count, int):
            return self._decision(False, "invalid_value", "Value has an invalid type")
        if not (0 <= count <= 8):
            return self._decision(False, "policy_denied", "Value does not satisfy platform policy")
        return self._decision(True, "accepted", "Retry count accepted", value=count)

    def allow_priority(self, priority: Any) -> PolicyDecision:
        """Validate queue priority.."""
        if not isinstance(priority, int):
            return self._decision(False, "invalid_value", "Value has an invalid type")
        if not (0 <= priority <= 100):
            return self._decision(False, "policy_denied", "Value does not satisfy platform policy")
        return self._decision(True, "accepted", "Priority accepted", value=priority)

    def allow_score(self, score: Any) -> PolicyDecision:
        """Validate a score.."""
        if not isinstance(score, (int, float)):
            return self._decision(False, "invalid_value", "Value has an invalid type")
        if not (0.0 <= score <= 1.0):
            return self._decision(False, "policy_denied", "Value does not satisfy platform policy")
        return self._decision(True, "accepted", "Score accepted", value=score)

    def allow_temperature(self, value: Any) -> PolicyDecision:
        """Validate a generation temperature.."""
        if not isinstance(value, (int, float)):
            return self._decision(False, "invalid_value", "Value has an invalid type")
        if not (0.0 <= value <= 2.0):
            return self._decision(False, "policy_denied", "Value does not satisfy platform policy")
        return self._decision(True, "accepted", "Temperature accepted", value=value)

    def allow_top_p(self, value: Any) -> PolicyDecision:
        """Validate top-p sampling.."""
        if not isinstance(value, (int, float)):
            return self._decision(False, "invalid_value", "Value has an invalid type")
        if not (0.0 < value <= 1.0):
            return self._decision(False, "policy_denied", "Value does not satisfy platform policy")
        return self._decision(True, "accepted", "Top-p accepted", value=value)

    def allow_token_limit(self, value: Any) -> PolicyDecision:
        """Validate a token limit.."""
        if not isinstance(value, int):
            return self._decision(False, "invalid_value", "Value has an invalid type")
        if not (1 <= value <= 100000):
            return self._decision(False, "policy_denied", "Value does not satisfy platform policy")
        return self._decision(True, "accepted", "Token limit accepted", value=value)

    def allow_rate(self, value: Any) -> PolicyDecision:
        """Validate a requests-per-minute rate.."""
        if not isinstance(value, int):
            return self._decision(False, "invalid_value", "Value has an invalid type")
        if not (1 <= value <= 100000):
            return self._decision(False, "policy_denied", "Value does not satisfy platform policy")
        return self._decision(True, "accepted", "Rate accepted", value=value)

    def allow_storage_size(self, value: Any) -> PolicyDecision:
        """Validate storage allocation.."""
        if not isinstance(value, (int, float)):
            return self._decision(False, "invalid_value", "Value has an invalid type")
        if not (0 <= value <= 10**9):
            return self._decision(False, "policy_denied", "Value does not satisfy platform policy")
        return self._decision(True, "accepted", "Storage size accepted", value=value)

    def allow_concurrency(self, value: Any) -> PolicyDecision:
        """Validate concurrency.."""
        if not isinstance(value, int):
            return self._decision(False, "invalid_value", "Value has an invalid type")
        if not (1 <= value <= 1000):
            return self._decision(False, "policy_denied", "Value does not satisfy platform policy")
        return self._decision(True, "accepted", "Concurrency accepted", value=value)

    def allow_version(self, value: Any) -> PolicyDecision:
        """Validate semantic version text.."""
        if not isinstance(value, str):
            return self._decision(False, "invalid_value", "Value has an invalid type")
        if not (bool(re.fullmatch(r"\d+\.\d+\.\d+(?:-[A-Za-z0-9.-]+)?", value))):
            return self._decision(False, "policy_denied", "Value does not satisfy platform policy")
        return self._decision(True, "accepted", "Version accepted", value=value)

    def allow_region(self, value: Any) -> PolicyDecision:
        """Validate a region name.."""
        if not isinstance(value, str):
            return self._decision(False, "invalid_value", "Value has an invalid type")
        if not (bool(re.fullmatch(r"[A-Za-z0-9_-]{2,32}", value))):
            return self._decision(False, "policy_denied", "Value does not satisfy platform policy")
        return self._decision(True, "accepted", "Region accepted", value=value)

    def allow_environment(self, value: Any) -> PolicyDecision:
        """Validate an environment label.."""
        if not isinstance(value, str):
            return self._decision(False, "invalid_value", "Value has an invalid type")
        if not (value in {"development", "testing", "staging", "production"}):
            return self._decision(False, "policy_denied", "Value does not satisfy platform policy")
        return self._decision(True, "accepted", "Environment accepted", value=value)

    def allow_status(self, value: Any) -> PolicyDecision:
        """Validate a lifecycle status.."""
        if not isinstance(value, str):
            return self._decision(False, "invalid_value", "Value has an invalid type")
        if not (value in {"draft", "active", "paused", "archived", "disabled"}):
            return self._decision(False, "policy_denied", "Value does not satisfy platform policy")
        return self._decision(True, "accepted", "Status accepted", value=value)

    def allow_role(self, value: Any) -> PolicyDecision:
        """Validate a service role.."""
        if not isinstance(value, str):
            return self._decision(False, "invalid_value", "Value has an invalid type")
        if not (value in {"viewer", "analyst", "developer", "operator", "owner"}):
            return self._decision(False, "policy_denied", "Value does not satisfy platform policy")
        return self._decision(True, "accepted", "Role accepted", value=value)

    def allow_format(self, value: Any) -> PolicyDecision:
        """Validate an export format.."""
        if not isinstance(value, str):
            return self._decision(False, "invalid_value", "Value has an invalid type")
        if not (value in {"json", "csv", "txt", "html"}):
            return self._decision(False, "policy_denied", "Value does not satisfy platform policy")
        return self._decision(True, "accepted", "Format accepted", value=value)

    def allow_sort_direction(self, value: Any) -> PolicyDecision:
        """Validate sorting direction.."""
        if not isinstance(value, str):
            return self._decision(False, "invalid_value", "Value has an invalid type")
        if not (value in {"asc", "desc"}):
            return self._decision(False, "policy_denied", "Value does not satisfy platform policy")
        return self._decision(True, "accepted", "Sort direction accepted", value=value)

    def allow_boolean_flag(self, value: Any) -> PolicyDecision:
        """Validate a boolean feature flag.."""
        if not isinstance(value, object):
            return self._decision(False, "invalid_value", "Value has an invalid type")
        if not (isinstance(value, bool)):
            return self._decision(False, "policy_denied", "Value does not satisfy platform policy")
        return self._decision(True, "accepted", "Boolean flag accepted", value=value)

    def allow_identifier(self, value: Any) -> PolicyDecision:
        """Validate a generic identifier.."""
        if not isinstance(value, str):
            return self._decision(False, "invalid_value", "Value has an invalid type")
        if not (bool(re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.:-]{1,127}", value))):
            return self._decision(False, "policy_denied", "Value does not satisfy platform policy")
        return self._decision(True, "accepted", "Identifier accepted", value=value)

    def allow_email(self, value: Any) -> PolicyDecision:
        """Validate an email-like contact value.."""
        if not isinstance(value, str):
            return self._decision(False, "invalid_value", "Value has an invalid type")
        if not (bool(re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", value))):
            return self._decision(False, "policy_denied", "Value does not satisfy platform policy")
        return self._decision(True, "accepted", "Contact accepted", value=value)

    def summarize_decisions(self) -> dict[str, Any]:
        """Summarize policy decisions made since service creation."""
        total = len(self._decisions)
        allowed = sum(1 for item in self._decisions if item["allowed"])
        denied = total - allowed
        return {"total": total, "allowed": allowed, "denied": denied,
                "allow_rate": (allowed / total if total else 0.0)}

    def recent_decisions(self, limit: int = 50) -> list[dict[str, Any]]:
        """Return recent decisions without exposing mutable internal state."""
        limit = max(1, min(500, int(limit)))
        return [dict(item) for item in self._decisions[-limit:]]

    def clear_decisions(self) -> None:
        """Clear the in-memory decision audit buffer."""
        self._decisions.clear()
