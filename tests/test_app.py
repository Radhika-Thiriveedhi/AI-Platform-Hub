import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app import create_app
from services.analytics_service import AnalyticsService
from services.validation_service import ValidationService, build_key, coerce_bool


def make_client():
    app = create_app({"TESTING": True, "SECRET_KEY": "test-only"})
    return app.test_client()


def test_home_page():
    response = make_client().get("/")
    assert response.status_code == 200
    assert b"AI Platform Hub" in response.data


def test_health_endpoint():
    response = make_client().get("/api/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "ok"


def test_models_endpoint():
    response = make_client().get("/api/models")
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)


def test_unknown_model_is_not_found():
    response = make_client().get("/api/models/not-a-real-model")
    assert response.status_code == 404


def test_chat_rejects_empty_message():
    response = make_client().post("/chat/send", json={"message": ""})
    assert response.status_code == 400


def test_chat_accepts_message():
    response = make_client().post("/chat/send", json={"message": "hello"})
    assert response.status_code == 200
    assert response.get_json()["status"] == "success"


def test_model_pagination_handles_bad_page():
    response = make_client().get("/models/?page=-5")
    assert response.status_code == 200


def test_service_lifecycle():
    service = AnalyticsService()
    item = service.put("sales", 42, labels=["KPI"])
    assert item.identifier == "sales"
    assert service.get("sales").value == 42
    assert service.delete("sales") is True
    assert service.get("sales") is None


def test_validation_service_helpers():
    assert ValidationService is not None
    from services.validation_service import normalize_name, paginate, validate_limit
    assert normalize_name("  Hello   World ") == "hello world"
    assert validate_limit(5, 10) == 5
    assert build_key("  Alice ", " Smith ") == "alice:smith"
    assert coerce_bool("true") is True
    assert coerce_bool("no") is False
    page, meta = paginate(list(range(5)), 2, 2)
    assert page == [2, 3]
    assert meta["pages"] == 3
