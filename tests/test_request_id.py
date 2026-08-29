"""Tests for the request tracing response header."""

from app import create_app


def test_request_id_is_generated_when_client_does_not_supply_one():
    client = create_app({"TESTING": True, "SECRET_KEY": "test-only"}).test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert response.headers["X-Request-ID"]


def test_request_id_honors_a_client_supplied_value():
    client = create_app({"TESTING": True, "SECRET_KEY": "test-only"}).test_client()

    response = client.get("/", headers={"X-Request-ID": "support-case-123"})

    assert response.headers["X-Request-ID"] == "support-case-123"
