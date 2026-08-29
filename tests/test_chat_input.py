"""Request parsing tests for the chat endpoint."""

from app import create_app


def test_chat_rejects_non_json_payload_with_a_clear_client_error():
    client = create_app({"TESTING": True, "SECRET_KEY": "test-only"}).test_client()

    response = client.post("/chat/send", data="not-json", content_type="text/plain")

    assert response.status_code == 400
    assert response.get_json() == {"error": "Empty message"}


def test_chat_rejects_malformed_json_with_a_clear_client_error():
    client = create_app({"TESTING": True, "SECRET_KEY": "test-only"}).test_client()

    response = client.post("/chat/send", data="{", content_type="application/json")

    assert response.status_code == 400
    assert response.get_json() == {"error": "Empty message"}
