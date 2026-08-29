"""Application factory and runtime configuration for AI Platform Hub."""
from __future__ import annotations

import os
import secrets
from flask import Flask, g, request
from app.routes import register_blueprints


def _secret_key() -> str:
    """Return a configured secret, generating a development-only fallback."""
    configured = os.getenv("SECRET_KEY", "").strip()
    if configured:
        return configured
    return secrets.token_hex(32)


def create_app(test_config: dict | None = None) -> Flask:
    """Create and configure the Flask application."""
    app = Flask(
        __name__,
        template_folder="../templates",
        static_folder="../static",
        static_url_path="/static",
    )
    app.config.update(
        SECRET_KEY=_secret_key(),
        TEMPLATES_AUTO_RELOAD=os.getenv("TEMPLATES_AUTO_RELOAD", "false").lower() == "true",
        SEND_FILE_MAX_AGE_DEFAULT=int(os.getenv("SEND_FILE_MAX_AGE", "0")),
        MAX_CONTENT_LENGTH=int(os.getenv("MAX_CONTENT_LENGTH", str(2 * 1024 * 1024))),
    )
    if test_config:
        app.config.update(test_config)

    register_blueprints(app)

    @app.before_request
    def assign_request_id():
        """Attach a stable request identifier for logs and client support."""
        supplied_id = request.headers.get("X-Request-ID", "").strip()
        g.request_id = supplied_id[:128] if supplied_id else secrets.token_hex(12)

    @app.after_request
    def add_security_headers(response):
        response.headers.setdefault("X-Content-Type-Options", "nosniff")
        response.headers.setdefault("X-Frame-Options", "SAMEORIGIN")
        response.headers.setdefault("Referrer-Policy", "strict-origin-when-cross-origin")
        response.headers["X-Request-ID"] = g.request_id
        return response

    @app.context_processor
    def inject_globals():
        return {"app_name": "AI Platform Hub", "app_version": "1.1.0", "current_year": 2026}

    return app
