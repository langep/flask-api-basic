"""Test exceptions.py."""

from {{cookiecutter.main_package_name}}.exceptions import ApiError


def test_api_error():
    """Test ApiError exception."""
    # Test message and default return code.
    api_error = ApiError('Some message')
    assert api_error.message == 'Some message'
    assert api_error.code == 400

    # Test message and specified return code.
    api_error = ApiError('Some message', code=402)
    assert api_error.message == 'Some message'
    assert api_error.code == 402
