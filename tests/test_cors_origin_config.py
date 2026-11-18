"""CORS origin parsing must fail closed and normalize explicit allowlists."""

import pytest

from core.middleware import parse_allowed_origins


def test_unset_and_blank_origins_default_to_loopback():
    expected = ["http://localhost", "http://127.0.0.1"]
    assert parse_allowed_origins(None) == expected
    assert parse_allowed_origins("  ") == expected
    assert parse_allowed_origins(" , , ") == expected


def test_explicit_origins_are_trimmed_and_deduplicated():
    assert parse_allowed_origins(
        " https://app.example.com,https://admin.example.com, https://app.example.com "
    ) == ["https://app.example.com", "https://admin.example.com"]


def test_wildcard_origin_is_rejected():
    with pytest.raises(ValueError, match="explicit origins"):
        parse_allowed_origins("*")


def test_mixed_wildcard_origin_is_rejected():
    with pytest.raises(ValueError, match="explicit origins"):
        parse_allowed_origins("https://app.example.com,*")
