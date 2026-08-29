"""Production quality-gate helpers for the AI Platform Hub.

This module provides deterministic checks used by the application before a
dataset, model, or workflow is promoted to the next lifecycle stage.
"""

from dataclasses import dataclass
from typing import Any, Mapping


@dataclass(frozen=True)
class QualityGateResult:
    """Result returned by a production quality gate."""

    passed: bool
    score: float
    checks: tuple[str, ...]
    messages: tuple[str, ...]


class QualityGateService:
    """Evaluate common readiness conditions without external connections."""

    def __init__(self, minimum_score: float = 0.70) -> None:
        self.minimum_score = max(0.0, min(1.0, minimum_score))

    def validate_dataset(self, profile: Mapping[str, Any]) -> QualityGateResult:
        """Check whether a dataset profile is ready for preprocessing."""
        checks: list[str] = []
        messages: list[str] = []
        score = 0.0

        rows = int(profile.get("rows", 0) or 0)
        columns = int(profile.get("columns", 0) or 0)
        missing_rate = float(profile.get("missing_rate", 1.0) or 0.0)
        duplicate_rate = float(profile.get("duplicate_rate", 1.0) or 0.0)

        if rows > 0:
            checks.append("non_empty_rows")
            score += 0.25
        else:
            messages.append("Dataset contains no rows.")

        if columns > 0:
            checks.append("non_empty_columns")
            score += 0.25
        else:
            messages.append("Dataset contains no columns.")

        if missing_rate <= 0.30:
            checks.append("missing_values_within_limit")
            score += 0.25
        else:
            messages.append("Missing-value rate exceeds the configured limit.")

        if duplicate_rate <= 0.20:
            checks.append("duplicates_within_limit")
            score += 0.25
        else:
            messages.append("Duplicate-row rate exceeds the configured limit.")

        return self._result(score, checks, messages)

    def validate_features(self, features: list[Mapping[str, Any]]) -> QualityGateResult:
        """Check feature definitions for stable names and supported types."""
        checks: list[str] = []
        messages: list[str] = []
        score = 0.0

        if features:
            checks.append("features_present")
            score += 0.25
        else:
            messages.append("No feature definitions were supplied.")

        names = [str(item.get("name", "")).strip() for item in features]
        if names and all(names):
            checks.append("feature_names_present")
            score += 0.25
        else:
            messages.append("Every feature must have a non-empty name.")

        if len(names) == len(set(names)) and names:
            checks.append("feature_names_unique")
            score += 0.25
        elif names:
            messages.append("Feature names must be unique.")

        supported = {"numeric", "categorical", "text", "datetime", "boolean"}
        declared = {
            str(item.get("type", "")).strip().lower()
            for item in features
            if item.get("type") is not None
        }
        if declared and declared.issubset(supported):
            checks.append("feature_types_supported")
            score += 0.25
        elif features:
            messages.append("One or more feature types are unsupported.")

        return self._result(score, checks, messages)

    def validate_training_run(self, metrics: Mapping[str, Any]) -> QualityGateResult:
        """Check model-training metrics for finite, meaningful values."""
        checks: list[str] = []
        messages: list[str] = []
        score = 0.0

        metric_names = ("accuracy", "precision", "recall", "f1")
        present = [name for name in metric_names if name in metrics]

        if present:
            checks.append("metrics_present")
            score += 0.25
        else:
            messages.append("No standard evaluation metrics were supplied.")

        valid = True
        for name in present:
            try:
                value = float(metrics[name])
            except (TypeError, ValueError):
                valid = False
                continue
            if not 0.0 <= value <= 1.0:
                valid = False

        if present and valid:
            checks.append("metrics_in_range")
            score += 0.25
        elif present:
            messages.append("Evaluation metrics must be between zero and one.")

        if metrics.get("training_samples", 0):
            checks.append("training_samples_recorded")
            score += 0.25
        else:
            messages.append("Training sample count is missing.")

        if metrics.get("validation_samples", 0):
            checks.append("validation_samples_recorded")
            score += 0.25
        else:
            messages.append("Validation sample count is missing.")

        return self._result(score, checks, messages)

    def promotion_allowed(self, result: QualityGateResult) -> bool:
        """Return whether a previously computed result meets the gate."""
        return result.passed and result.score >= self.minimum_score

    def summarize(self, result: QualityGateResult) -> dict[str, Any]:
        """Convert a gate result into a serializable application response."""
        return {
            "passed": result.passed,
            "score": round(result.score, 4),
            "minimum_score": self.minimum_score,
            "checks": list(result.checks),
            "messages": list(result.messages),
            "promotion_allowed": self.promotion_allowed(result),
        }

    def _result(
        self,
        score: float,
        checks: list[str],
        messages: list[str],
    ) -> QualityGateResult:
        """Build a normalized immutable gate result."""
        normalized = max(0.0, min(1.0, float(score)))
        passed = normalized >= self.minimum_score and not messages
        return QualityGateResult(
            passed=passed,
            score=normalized,
            checks=tuple(checks),
            messages=tuple(messages),
        )
