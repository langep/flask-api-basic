"""Tests for correct error handling."""
from tests.assertion_helpers import assert_json_response_headers


class TestErrors():
    """Test errors."""

    def test_notfound(self, testapp):
        """Test 404 error page."""
        resp = testapp.get('/doesnotexist', status=404)
        # Response headers
        assert_json_response_headers(resp)
        # Response body
        body = resp.json
        assert body['error']['code'] == 404
        assert body['error']['message'] == 'Not Found'
