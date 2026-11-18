"""Security configuration defaults must not permit wildcard CORS origins."""

from src.config import SecurityConfig


def test_security_config_defaults_to_loopback_origins(monkeypatch):
    monkeypatch.delenv("SECURITY_ALLOWED_ORIGINS", raising=False)

    config = SecurityConfig(_env_file=None)

    assert config.allowed_origins == ["http://localhost", "http://127.0.0.1"]
    assert "*" not in config.allowed_origins


def test_security_config_accepts_explicit_origins(monkeypatch):
    monkeypatch.setenv(
        "SECURITY_ALLOWED_ORIGINS",
        '["https://app.example.com","https://admin.example.com"]',
    )

    config = SecurityConfig(_env_file=None)

    assert config.allowed_origins == [
        "https://app.example.com",
        "https://admin.example.com",
    ]
