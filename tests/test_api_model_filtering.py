"""Tests for model catalog API filtering."""

from app import create_app


def make_client():
    return create_app({"TESTING": True, "SECRET_KEY": "test-only"}).test_client()


def test_models_api_filters_by_category():
    response = make_client().get("/api/models?category=Large%20Language%20Models")

    assert response.status_code == 200
    assert response.get_json()
    assert all(model["category"] == "Large Language Models" for model in response.get_json())


def test_models_api_filters_by_search_query():
    response = make_client().get("/api/models?q=OpenAI")

    assert response.status_code == 200
    assert response.get_json()
    assert all(model["provider"] == "OpenAI" for model in response.get_json())
