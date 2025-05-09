import pytest
import requests
from requests.auth import HTTPBasicAuth

@pytest.mark.auth
def test_basic_auth():
	response = requests.get(
		"https://httpbin.org/basic-auth/user/passwd",
		auth=HTTPBasicAuth("user", "passwd")
	)
	assert response.status_code == 200
	assert response.json()["authenticated"] is True

@pytest.mark.auth
def test_bearer_token_auth():
	headers = {"Authorization": "Bearer fake-token-123"}
	response = requests.get("https://httpbin.org/bearer", headers=headers)
	assert response.status_code == 200
	assert response.json()["authenticated"] is True