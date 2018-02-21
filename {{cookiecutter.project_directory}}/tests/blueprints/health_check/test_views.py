"""Tests for health_check blueprint."""

from tests.assertion_helpers import (
    assert_get_only,
    assert_json_response_headers
)


class TestHealthCheckBlueprint():
    """Test health_check blueprint."""

    def test_health_check(self, testapp):
        """Assert health_check endpoint functionality."""
        resp = testapp.get('/health_check')
        # Response headers
        assert_json_response_headers(resp)
        # Response body
        body = resp.json
        assert body['success']

    def test_get_only(self, testapp):
        """Assert health_check endpoint is GET only."""
        assert_get_only(
            '/health_check',
            testapp
        )
