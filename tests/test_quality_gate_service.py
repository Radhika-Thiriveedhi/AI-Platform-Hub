from services.quality_gate_service import QualityGateService


def test_quality_gate_passes_for_ready_dataset():
    service = QualityGateService()
    result = service.validate_dataset({
        "rows": 5000,
        "columns": 12,
        "missing_rate": 0.12,
        "duplicate_rate": 0.05,
    })

    assert result.passed is True
    assert result.score >= service.minimum_score
    assert "missing_values_within_limit" in result.checks


def test_quality_gate_rejects_incomplete_feature_definitions():
    service = QualityGateService()
    result = service.validate_features([
        {"name": "age", "type": "numeric"},
        {"name": "", "type": "text"},
    ])

    assert result.passed is False
    assert "Every feature must have a non-empty name." in result.messages


def test_quality_gate_validates_training_metrics_range():
    service = QualityGateService()
    result = service.validate_training_run({
        "accuracy": 0.94,
        "precision": 0.9,
        "recall": 0.88,
        "f1": 0.91,
        "training_samples": 1000,
        "validation_samples": 250,
    })

    assert result.passed is True
    assert result.score >= 0.75
