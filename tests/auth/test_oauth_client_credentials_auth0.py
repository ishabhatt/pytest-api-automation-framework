from utils.auth0_client import Auth0Client
import pytest

@pytest.mark.auth
def test_auth0_api_user_read():
	client = Auth0Client()
	users = client.get("users")
	assert isinstance(users, list) or "users" in users  # depends on your API