"""Defines common assertion helpers."""


def assert_json_response_headers(response):
    """Assert if response headers are correct for JSON response.

    Args:
        respone: WebTest response object.

    """
    assert response.content_type == 'application/json'
    assert response.content_length > 0


def assert_get_only(path, testapp):
    """Assert if endpoint allows only GET request.

    Args:
        path: The endpoint to test.
        testapp: Flask app testclient object.

    """
    def assert_body(response):
        body = resp.json
        assert body['error']['code'] == 405
        assert body['error']['message'] == 'Method Not Allowed'

    # POST
    resp = testapp.post(path, status=405)
    assert_json_response_headers(resp)
    assert_body(resp)

    # PUT
    resp = testapp.put(path, status=405)
    assert_json_response_headers(resp)
    assert_body(resp)

    # DELETE
    resp = testapp.delete(path, status=405)
    assert_json_response_headers(resp)
    assert_body(resp)
