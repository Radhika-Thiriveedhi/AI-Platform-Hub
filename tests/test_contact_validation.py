"""Validation tests for contact form submissions."""

from app import create_app


def make_client():
    return create_app({"TESTING": True, "SECRET_KEY": "test-only"}).test_client()


def test_contact_form_rejects_an_invalid_email_address():
    response = make_client().post(
        "/contact",
        data={"name": "Ada", "email": "not-an-email", "message": "Please contact me."},
    )

    assert response.status_code == 200
    assert b"Please provide a name, a valid email address, and a message." in response.data


def test_contact_form_accepts_a_valid_email_address():
    response = make_client().post(
        "/contact",
        data={"name": "Ada", "email": "ada@example.com", "message": "Please contact me."},
    )

    assert response.status_code == 200
    assert b"Thank you Ada!" in response.data
