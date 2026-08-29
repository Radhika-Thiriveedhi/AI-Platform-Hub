"""Production-oriented ML lifecycle helpers for AI Platform Hub.

The service is deliberately dependency-light and database-free. It provides
small, composable operations for dataset readiness, feature definitions,
training runs, model promotion, deployment checks, and operational scoring.
All state is held in memory so the HTTP application can use the service in a
local development environment without external infrastructure.
"""
from __future__ import annotations

from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from typing import Any, Iterable, Mapping, Sequence
import hashlib
import math
import statistics


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _clean(value: Any) -> str:
    return str(value).strip()


def _finite(value: Any, default: float = 0.0) -> float:
    try:
        number = float(value)
    except (TypeError, ValueError):
        return default
    return number if math.isfinite(number) else default


@dataclass(slots=True)
class DatasetProfile:
    name: str
    rows: int = 0
    columns: int = 0
    missing_rate: float = 0.0
    duplicate_rate: float = 0.0
    numeric_columns: int = 0
    categorical_columns: int = 0
    target_column: str | None = None
    status: str = "draft"
    created_at: str = field(default_factory=_now)

    @property
    def completeness(self) -> float:
        return max(0.0, min(1.0, 1.0 - self.missing_rate))

    @property
    def uniqueness(self) -> float:
        return max(0.0, min(1.0, 1.0 - self.duplicate_rate))

    @property
    def readiness_score(self) -> float:
        volume = min(1.0, self.rows / 1000.0) if self.rows else 0.0
        schema = min(1.0, self.columns / 10.0) if self.columns else 0.0
        return round((self.completeness * 0.45 + self.uniqueness * 0.25 + volume * 0.2 + schema * 0.1) * 100, 2)

    def to_dict(self) -> dict[str, Any]:
        result = asdict(self)
        result["completeness"] = round(self.completeness, 4)
        result["uniqueness"] = round(self.uniqueness, 4)
        result["readiness_score"] = self.readiness_score
        return result


@dataclass(slots=True)
class FeatureDefinition:
    name: str
    source_column: str
    feature_type: str = "numeric"
    transformation: str = "identity"
    nullable: bool = True
    description: str = ""
    owner: str = "platform"
    version: int = 1
    status: str = "active"
    created_at: str = field(default_factory=_now)

    def signature(self) -> str:
        raw = "|".join([self.name, self.source_column, self.feature_type, self.transformation, str(self.version)])
        return hashlib.sha256(raw.encode()).hexdigest()[:16]

    def to_dict(self) -> dict[str, Any]:
        result = asdict(self)
        result["signature"] = self.signature()
        return result


@dataclass(slots=True)
class TrainingRun:
    run_id: str
    model_name: str
    dataset: str
    features: list[str] = field(default_factory=list)
    algorithm: str = "baseline"
    metrics: dict[str, float] = field(default_factory=dict)
    parameters: dict[str, Any] = field(default_factory=dict)
    status: str = "queued"
    created_at: str = field(default_factory=_now)
    completed_at: str | None = None

    @property
    def primary_score(self) -> float:
        for key in ("f1", "accuracy", "roc_auc", "r2", "precision", "recall"):
            if key in self.metrics:
                return _finite(self.metrics[key])
        return 0.0

    def finish(self, metrics: Mapping[str, Any]) -> None:
        self.metrics = {str(k): _finite(v) for k, v in metrics.items()}
        self.status = "completed"
        self.completed_at = _now()

    def to_dict(self) -> dict[str, Any]:
        result = asdict(self)
        result["primary_score"] = self.primary_score
        return result


@dataclass(slots=True)
class ModelVersion:
    model_name: str
    version: str
    run_id: str
    score: float
    stage: str = "candidate"
    artifact_hash: str = ""
    notes: str = ""
    created_at: str = field(default_factory=_now)

    def promote(self, stage: str) -> None:
        allowed = {"candidate", "staging", "production", "retired"}
        clean = _clean(stage).lower()
        if clean not in allowed:
            raise ValueError("unsupported model stage")
        self.stage = clean

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(slots=True)
class DeploymentCheck:
    name: str
    passed: bool
    severity: str = "info"
    message: str = ""

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


class MLOpsLifecycleService:
    """Coordinate lightweight, deterministic ML lifecycle state."""

    SUPPORTED_ALGORITHMS = {
        "baseline", "logistic_regression", "random_forest", "gradient_boosting",
        "linear_regression", "xgboost", "lightgbm", "svm", "knn", "naive_bayes",
    }
    FEATURE_TYPES = {"numeric", "categorical", "boolean", "text", "datetime"}
    TRANSFORMATIONS = {
        "identity", "standardize", "normalize", "log1p", "clip", "bucket", "one_hot",
        "ordinal", "frequency", "target_encode", "date_parts", "text_length",
    }

    def __init__(self) -> None:
        self.datasets: dict[str, DatasetProfile] = {}
        self.features: dict[str, FeatureDefinition] = {}
        self.runs: dict[str, TrainingRun] = {}
        self.models: dict[tuple[str, str], ModelVersion] = {}
        self.checks: dict[str, list[DeploymentCheck]] = {}

    def register_dataset(self, profile: DatasetProfile | Mapping[str, Any]) -> DatasetProfile:
        item = self._coerce_dataset(profile)
        if not item.name:
            raise ValueError("dataset name is required")
        if item.rows < 0 or item.columns < 0:
            raise ValueError("dataset dimensions cannot be negative")
        item.missing_rate = max(0.0, min(1.0, item.missing_rate))
        item.duplicate_rate = max(0.0, min(1.0, item.duplicate_rate))
        item.status = "ready" if item.readiness_score >= 60 else "needs_review"
        self.datasets[item.name] = item
        return item

    def _coerce_dataset(self, value: DatasetProfile | Mapping[str, Any]) -> DatasetProfile:
        if isinstance(value, DatasetProfile):
            return value
        return DatasetProfile(
            name=_clean(value.get("name", "")),
            rows=int(value.get("rows", 0) or 0),
            columns=int(value.get("columns", 0) or 0),
            missing_rate=_finite(value.get("missing_rate", 0.0)),
            duplicate_rate=_finite(value.get("duplicate_rate", 0.0)),
            numeric_columns=int(value.get("numeric_columns", 0) or 0),
            categorical_columns=int(value.get("categorical_columns", 0) or 0),
            target_column=value.get("target_column"),
        )

    def get_dataset(self, name: str) -> DatasetProfile | None:
        return self.datasets.get(_clean(name))

    def list_datasets(self, status: str | None = None) -> list[DatasetProfile]:
        items = list(self.datasets.values())
        if status:
            clean = _clean(status).lower()
            items = [item for item in items if item.status == clean]
        return sorted(items, key=lambda item: item.name.lower())

    def remove_dataset(self, name: str) -> bool:
        return self.datasets.pop(_clean(name), None) is not None

    def dataset_health(self, name: str) -> dict[str, Any]:
        dataset = self.get_dataset(name)
        if dataset is None:
            raise KeyError("dataset not found")
        checks = {
            "volume": dataset.rows >= 100,
            "schema": dataset.columns >= 2,
            "missingness": dataset.missing_rate <= 0.2,
            "duplicates": dataset.duplicate_rate <= 0.2,
            "target": bool(dataset.target_column),
        }
        passed = sum(checks.values())
        return {"dataset": dataset.name, "score": dataset.readiness_score, "checks": checks, "passed": passed, "total": len(checks)}

    def define_feature(self, feature: FeatureDefinition | Mapping[str, Any]) -> FeatureDefinition:
        item = self._coerce_feature(feature)
        if not item.name or not item.source_column:
            raise ValueError("feature name and source column are required")
        if item.feature_type not in self.FEATURE_TYPES:
            raise ValueError("unsupported feature type")
        if item.transformation not in self.TRANSFORMATIONS:
            raise ValueError("unsupported transformation")
        existing = self.features.get(item.name)
        if existing:
            item.version = existing.version + 1
        self.features[item.name] = item
        return item

    def _coerce_feature(self, value: FeatureDefinition | Mapping[str, Any]) -> FeatureDefinition:
        if isinstance(value, FeatureDefinition):
            return value
        return FeatureDefinition(
            name=_clean(value.get("name", "")),
            source_column=_clean(value.get("source_column", "")),
            feature_type=_clean(value.get("feature_type", "numeric")).lower(),
            transformation=_clean(value.get("transformation", "identity")).lower(),
            nullable=bool(value.get("nullable", True)),
            description=_clean(value.get("description", "")),
            owner=_clean(value.get("owner", "platform")),
        )

    def get_feature(self, name: str) -> FeatureDefinition | None:
        return self.features.get(_clean(name))

    def list_features(self, owner: str | None = None) -> list[FeatureDefinition]:
        items = list(self.features.values())
        if owner:
            items = [item for item in items if item.owner == _clean(owner)]
        return sorted(items, key=lambda item: item.name.lower())

    def retire_feature(self, name: str) -> FeatureDefinition:
        feature = self.get_feature(name)
        if feature is None:
            raise KeyError("feature not found")
        feature.status = "retired"
        return feature

    def validate_feature_set(self, names: Sequence[str]) -> dict[str, Any]:
        clean_names = [_clean(name) for name in names]
        missing = [name for name in clean_names if name not in self.features]
        retired = [name for name in clean_names if name in self.features and self.features[name].status == "retired"]
        duplicates = sorted({name for name in clean_names if clean_names.count(name) > 1})
        return {"valid": not missing and not retired and not duplicates, "missing": missing, "retired": retired, "duplicates": duplicates, "count": len(clean_names)}

    def start_training(
        self,
        model_name: str,
        dataset: str,
        features: Sequence[str],
        algorithm: str = "baseline",
        parameters: Mapping[str, Any] | None = None,
    ) -> TrainingRun:
        name = _clean(model_name)
        dataset_name = _clean(dataset)
        algorithm_name = _clean(algorithm).lower()
        if not name or not dataset_name:
            raise ValueError("model name and dataset are required")
        if dataset_name not in self.datasets:
            raise KeyError("dataset not found")
        if algorithm_name not in self.SUPPORTED_ALGORITHMS:
            raise ValueError("unsupported algorithm")
        feature_check = self.validate_feature_set(features)
        if not feature_check["valid"]:
            raise ValueError("invalid feature set")
        raw_id = f"{name}|{dataset_name}|{len(self.runs) + 1}|{_now()}"
        run_id = hashlib.sha1(raw_id.encode()).hexdigest()[:12]
        run = TrainingRun(run_id=run_id, model_name=name, dataset=dataset_name, features=list(features), algorithm=algorithm_name, parameters=dict(parameters or {}), status="running")
        self.runs[run_id] = run
        return run

    def complete_training(self, run_id: str, metrics: Mapping[str, Any]) -> TrainingRun:
        run = self.runs.get(_clean(run_id))
        if run is None:
            raise KeyError("training run not found")
        if run.status not in {"running", "queued"}:
            raise ValueError("training run is already complete")
        run.finish(metrics)
        return run

    def fail_training(self, run_id: str, reason: str) -> TrainingRun:
        run = self.runs.get(_clean(run_id))
        if run is None:
            raise KeyError("training run not found")
        run.status = "failed"
        run.parameters["failure_reason"] = _clean(reason)
        run.completed_at = _now()
        return run

    def get_run(self, run_id: str) -> TrainingRun | None:
        return self.runs.get(_clean(run_id))

    def list_runs(self, model_name: str | None = None, status: str | None = None) -> list[TrainingRun]:
        items = list(self.runs.values())
        if model_name:
            items = [item for item in items if item.model_name == _clean(model_name)]
        if status:
            items = [item for item in items if item.status == _clean(status).lower()]
        return sorted(items, key=lambda item: item.created_at, reverse=True)

    def compare_runs(self, run_ids: Sequence[str]) -> list[dict[str, Any]]:
        result = []
        for run_id in run_ids:
            run = self.get_run(run_id)
            if run:
                result.append({"run_id": run.run_id, "model": run.model_name, "algorithm": run.algorithm, "score": run.primary_score, "status": run.status})
        return sorted(result, key=lambda item: item["score"], reverse=True)

    def register_model(self, model_name: str, version: str, run_id: str, score: float | None = None, notes: str = "") -> ModelVersion:
        run = self.get_run(run_id)
        if run is None:
            raise KeyError("training run not found")
        if run.status != "completed":
            raise ValueError("training run must be completed")
        value = run.primary_score if score is None else _finite(score)
        artifact_hash = hashlib.sha256(f"{model_name}|{version}|{run_id}".encode()).hexdigest()
        model = ModelVersion(model_name=_clean(model_name), version=_clean(version), run_id=run.run_id, score=value, artifact_hash=artifact_hash, notes=_clean(notes))
        self.models[(model.model_name, model.version)] = model
        return model

    def get_model(self, model_name: str, version: str) -> ModelVersion | None:
        return self.models.get((_clean(model_name), _clean(version)))

    def list_models(self, stage: str | None = None) -> list[ModelVersion]:
        items = list(self.models.values())
        if stage:
            items = [item for item in items if item.stage == _clean(stage).lower()]
        return sorted(items, key=lambda item: (item.model_name.lower(), item.version))

    def promote_model(self, model_name: str, version: str, stage: str) -> ModelVersion:
        model = self.get_model(model_name, version)
        if model is None:
            raise KeyError("model version not found")
        clean = _clean(stage).lower()
        if clean == "production":
            checks = self.run_deployment_checks(model_name, version)
            if not all(check.passed for check in checks if check.severity == "blocker"):
                raise ValueError("model failed production checks")
            for existing in self.list_models():
                if existing.model_name == model.model_name and existing.stage == "production":
                    existing.stage = "retired"
        model.promote(clean)
        return model

    def run_deployment_checks(self, model_name: str, version: str) -> list[DeploymentCheck]:
        model = self.get_model(model_name, version)
        if model is None:
            raise KeyError("model version not found")
        run = self.get_run(model.run_id)
        checks = [
            DeploymentCheck("artifact", bool(model.artifact_hash), "blocker", "Artifact fingerprint is available" if model.artifact_hash else "Missing artifact fingerprint"),
            DeploymentCheck("training", bool(run and run.status == "completed"), "blocker", "Training completed" if run and run.status == "completed" else "Training is incomplete"),
            DeploymentCheck("quality", model.score >= 0.5, "blocker", "Model score meets minimum threshold" if model.score >= 0.5 else "Model score is below threshold"),
            DeploymentCheck("version", bool(model.version), "warning", "Version is declared" if model.version else "Version is missing"),
            DeploymentCheck("traceability", bool(model.run_id), "warning", "Training run is linked" if model.run_id else "Training run is missing"),
        ]
        self.checks[f"{model.model_name}:{model.version}"] = checks
        return checks

    def deployment_summary(self, model_name: str, version: str) -> dict[str, Any]:
        checks = self.run_deployment_checks(model_name, version)
        blockers = [check for check in checks if check.severity == "blocker"]
        warnings = [check for check in checks if check.severity == "warning" and not check.passed]
        return {"model": _clean(model_name), "version": _clean(version), "ready": all(check.passed for check in blockers), "blockers": [c.message for c in blockers if not c.passed], "warnings": [c.message for c in warnings], "checks": [c.to_dict() for c in checks]}

    def model_health(self, model_name: str, version: str, observed_scores: Iterable[float] | None = None) -> dict[str, Any]:
        model = self.get_model(model_name, version)
        if model is None:
            raise KeyError("model version not found")
        values = [_finite(value) for value in (observed_scores or [])]
        baseline = model.score
        mean = statistics.fmean(values) if values else baseline
        drift = abs(mean - baseline)
        status = "healthy" if drift <= 0.1 else "watch" if drift <= 0.2 else "degraded"
        return {"model": model.model_name, "version": model.version, "baseline": baseline, "observed_mean": round(mean, 6), "drift": round(drift, 6), "status": status, "samples": len(values)}

    def snapshot(self) -> dict[str, Any]:
        return {
            "datasets": [item.to_dict() for item in self.list_datasets()],
            "features": [item.to_dict() for item in self.list_features()],
            "runs": [item.to_dict() for item in self.list_runs()],
            "models": [item.to_dict() for item in self.list_models()],
            "generated_at": _now(),
        }

    def clear(self) -> None:
        self.datasets.clear()
        self.features.clear()
        self.runs.clear()
        self.models.clear()
        self.checks.clear()

    def seed_demo(self) -> dict[str, Any]:
        """Populate a small deterministic lifecycle example for the UI."""
        self.register_dataset({"name": "customer_churn_demo", "rows": 5000, "columns": 12, "missing_rate": 0.04, "duplicate_rate": 0.02, "numeric_columns": 8, "categorical_columns": 4, "target_column": "churn"})
        for name, source, transform in [
            ("tenure_scaled", "tenure_months", "standardize"),
            ("monthly_spend_log", "monthly_spend", "log1p"),
            ("contract_frequency", "contract_type", "frequency"),
            ("support_tickets", "ticket_count", "clip"),
            ("is_auto_pay", "auto_pay", "identity"),
        ]:
            self.define_feature({"name": name, "source_column": source, "transformation": transform, "description": f"Derived feature from {source}"})
        run = self.start_training("churn_model", "customer_churn_demo", list(self.features), "random_forest", {"trees": 200, "seed": 42})
        self.complete_training(run.run_id, {"accuracy": 0.91, "precision": 0.88, "recall": 0.84, "f1": 0.86, "roc_auc": 0.94})
        model = self.register_model("churn_model", "1.0.0", run.run_id)
        return {"dataset": self.get_dataset("customer_churn_demo").to_dict(), "run": run.to_dict(), "model": model.to_dict()}

    # Reporting helpers keep UI routes free from lifecycle bookkeeping.
    def kpi(self) -> dict[str, Any]:
        completed = [run for run in self.runs.values() if run.status == "completed"]
        production = [model for model in self.models.values() if model.stage == "production"]
        ready = 0
        for model in self.models.values():
            try:
                if self.deployment_summary(model.model_name, model.version)["ready"]:
                    ready += 1
            except KeyError:
                continue
        return {
            "datasets": len(self.datasets),
            "features": len(self.features),
            "training_runs": len(self.runs),
            "completed_runs": len(completed),
            "models": len(self.models),
            "production_models": len(production),
            "deployment_ready_models": ready,
        }

    def training_success_rate(self) -> float:
        finished = [run for run in self.runs.values() if run.status in {"completed", "failed"}]
        if not finished:
            return 0.0
        return round(sum(run.status == "completed" for run in finished) / len(finished) * 100, 2)

    def average_model_score(self, model_name: str | None = None) -> float:
        models = list(self.models.values())
        if model_name:
            models = [model for model in models if model.model_name == _clean(model_name)]
        if not models:
            return 0.0
        return round(statistics.fmean(model.score for model in models), 6)

    def best_model(self, model_name: str | None = None) -> ModelVersion | None:
        models = list(self.models.values())
        if model_name:
            models = [model for model in models if model.model_name == _clean(model_name)]
        return max(models, key=lambda model: model.score, default=None)

    def audit_model_versions(self, model_name: str) -> list[dict[str, Any]]:
        models = [model for model in self.models.values() if model.model_name == _clean(model_name)]
        return [
            {
                "version": model.version,
                "stage": model.stage,
                "score": model.score,
                "run_id": model.run_id,
                "artifact_hash": model.artifact_hash,
                "created_at": model.created_at,
            }
            for model in sorted(models, key=lambda item: item.created_at)
        ]

    def feature_usage(self, feature_name: str) -> dict[str, Any]:
        clean = _clean(feature_name)
        feature = self.get_feature(clean)
        if feature is None:
            raise KeyError("feature not found")
        runs = [run.run_id for run in self.runs.values() if clean in run.features]
        return {"feature": clean, "version": feature.version, "status": feature.status, "training_runs": runs, "usage_count": len(runs)}

    def dataset_usage(self, dataset_name: str) -> dict[str, Any]:
        clean = _clean(dataset_name)
        dataset = self.get_dataset(clean)
        if dataset is None:
            raise KeyError("dataset not found")
        runs = [run.run_id for run in self.runs.values() if run.dataset == clean]
        return {"dataset": clean, "status": dataset.status, "training_runs": runs, "usage_count": len(runs)}

    def validate_training_parameters(self, algorithm: str, parameters: Mapping[str, Any] | None = None) -> dict[str, Any]:
        name = _clean(algorithm).lower()
        params = dict(parameters or {})
        errors: list[str] = []
        warnings: list[str] = []
        if name not in self.SUPPORTED_ALGORITHMS:
            errors.append("algorithm is not supported")
        if "seed" in params and not isinstance(params["seed"], int):
            errors.append("seed must be an integer")
        for key in ("trees", "estimators", "epochs"):
            if key in params and _finite(params[key], -1) < 1:
                errors.append(f"{key} must be positive")
        if name in {"random_forest", "gradient_boosting"} and "trees" not in params:
            warnings.append("tree count uses the application default")
        if name == "baseline":
            warnings.append("baseline is intended for benchmarking")
        return {"valid": not errors, "algorithm": name, "errors": errors, "warnings": warnings}

    def training_plan(self, model_name: str, dataset: str, features: Sequence[str], algorithm: str, parameters: Mapping[str, Any] | None = None) -> dict[str, Any]:
        feature_check = self.validate_feature_set(features)
        parameter_check = self.validate_training_parameters(algorithm, parameters)
        dataset_exists = self.get_dataset(dataset) is not None
        return {
            "model_name": _clean(model_name),
            "dataset": _clean(dataset),
            "feature_count": len(features),
            "features_valid": feature_check["valid"],
            "dataset_available": dataset_exists,
            "parameters": parameter_check,
            "ready": feature_check["valid"] and parameter_check["valid"] and dataset_exists,
        }

    def retrain_recommendation(self, model_name: str, observed_scores: Iterable[float] | None = None) -> dict[str, Any]:
        model = self.best_model(model_name)
        if model is None:
            return {"model": _clean(model_name), "action": "train", "reason": "no registered model"}
        health = self.model_health(model.model_name, model.version, observed_scores)
        if health["status"] == "degraded":
            action = "retrain_immediately"
        elif health["status"] == "watch":
            action = "monitor_and_retrain_if_trend_continues"
        else:
            action = "continue_monitoring"
        return {"model": model.model_name, "version": model.version, "action": action, "health": health}

    def lifecycle_report(self) -> dict[str, Any]:
        scores = [model.score for model in self.models.values()]
        return {
            "kpi": self.kpi(),
            "training_success_rate": self.training_success_rate(),
            "average_model_score": round(statistics.fmean(scores), 6) if scores else 0.0,
            "best_model": self.best_model().to_dict() if self.best_model() else None,
            "dataset_health": [self.dataset_health(item.name) for item in self.list_datasets()],
            "generated_at": _now(),
        }

    def export_rows(self) -> list[dict[str, Any]]:
        rows: list[dict[str, Any]] = []
        for model in self.list_models():
            rows.append({
                "model": model.model_name,
                "version": model.version,
                "stage": model.stage,
                "score": model.score,
                "run_id": model.run_id,
                "artifact_hash": model.artifact_hash,
            })
        return rows

    def import_dataset_rows(self, rows: Iterable[Mapping[str, Any]]) -> list[DatasetProfile]:
        imported: list[DatasetProfile] = []
        for row in rows:
            imported.append(self.register_dataset(row))
        return imported

    def import_feature_rows(self, rows: Iterable[Mapping[str, Any]]) -> list[FeatureDefinition]:
        imported: list[FeatureDefinition] = []
        for row in rows:
            imported.append(self.define_feature(row))
        return imported

    def remove_feature(self, name: str) -> bool:
        return self.features.pop(_clean(name), None) is not None

    def remove_run(self, run_id: str) -> bool:
        return self.runs.pop(_clean(run_id), None) is not None

    def remove_model(self, model_name: str, version: str) -> bool:
        return self.models.pop((_clean(model_name), _clean(version)), None) is not None

    def counts_by_stage(self) -> dict[str, int]:
        counts: dict[str, int] = {}
        for model in self.models.values():
            counts[model.stage] = counts.get(model.stage, 0) + 1
        return counts

    def counts_by_algorithm(self) -> dict[str, int]:
        counts: dict[str, int] = {}
        for run in self.runs.values():
            counts[run.algorithm] = counts.get(run.algorithm, 0) + 1
        return counts

    def counts_by_dataset(self) -> dict[str, int]:
        counts: dict[str, int] = {}
        for run in self.runs.values():
            counts[run.dataset] = counts.get(run.dataset, 0) + 1
        return counts

    def search_models(self, query: str) -> list[ModelVersion]:
        term = _clean(query).lower()
        if not term:
            return self.list_models()
        return [model for model in self.list_models() if term in model.model_name.lower() or term in model.version.lower() or term in model.stage.lower()]

    def search_features(self, query: str) -> list[FeatureDefinition]:
        term = _clean(query).lower()
        if not term:
            return self.list_features()
        return [feature for feature in self.list_features() if term in feature.name.lower() or term in feature.source_column.lower() or term in feature.transformation.lower()]

    def search_datasets(self, query: str) -> list[DatasetProfile]:
        term = _clean(query).lower()
        if not term:
            return self.list_datasets()
        return [dataset for dataset in self.list_datasets() if term in dataset.name.lower() or term in dataset.status.lower()]

    def readiness_matrix(self) -> list[dict[str, Any]]:
        matrix: list[dict[str, Any]] = []
        for dataset in self.list_datasets():
            health = self.dataset_health(dataset.name)
            matrix.append({"dataset": dataset.name, "readiness": dataset.readiness_score, "passed": health["passed"], "checks": health["total"]})
        return matrix

    def model_score_distribution(self) -> dict[str, float]:
        scores = [model.score for model in self.models.values()]
        if not scores:
            return {"min": 0.0, "max": 0.0, "mean": 0.0, "median": 0.0}
        return {"min": min(scores), "max": max(scores), "mean": statistics.fmean(scores), "median": statistics.median(scores)}

    def operational_summary(self) -> dict[str, Any]:
        return {
            "training_success_rate": self.training_success_rate(),
            "model_scores": self.model_score_distribution(),
            "stage_counts": self.counts_by_stage(),
            "algorithm_counts": self.counts_by_algorithm(),
            "dataset_usage": self.counts_by_dataset(),
            "feature_count": len(self.features),
        }
