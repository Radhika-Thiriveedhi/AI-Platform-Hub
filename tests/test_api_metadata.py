import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app import create_app


def test_api_health_includes_metadata():
    app = create_app({"TESTING": True, "SECRET_KEY": "test-only"})
    client = app.test_client()

    response = client.get("/api/health")

    assert response.status_code == 200
    payload = response.get_json()
    assert payload["status"] == "ok"
    assert payload["service"] == "AI Platform Hub"
    assert payload["version"] == "1.1.0"
    assert "checks" in payload


def test_api_stats_include_metadata_wrapper():
    app = create_app({"TESTING": True, "SECRET_KEY": "test-only"})
    client = app.test_client()

    response = client.get("/api/stats")

    assert response.status_code == 200
    payload = response.get_json()
    assert payload["status"] == "ok"
    assert payload["service"] == "AI Platform Hub"
    assert "data" in payload
