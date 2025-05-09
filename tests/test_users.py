import pytest
from utils.api_client import APIClient
from utils.schema_validator import UserResponse, CreateUserResponse, LoginSuccessResponse, LoginFailureResponse

client = APIClient()

@pytest.mark.smoke
def test_get_users():
	response = client.get("/users", params={"page": 2})
	assert response.status_code == 200
	parsed = UserResponse(**response.json())
	assert parsed.page == 2

@pytest.mark.regression
def test_create_user():
	payload = {"name": "morpheus", "job": "leader"}
	response = client.post("/users", json=payload)
	assert response.status_code == 201
	parsed = CreateUserResponse(**response.json())
	assert parsed.name == "morpheus"
	assert parsed.job == "leader"

@pytest.mark.regression
def test_update_user():
	payload = {"name": "neo", "job": "the one"}
	response = client.put("/users/2", json=payload)
	assert response.status_code == 200
	assert response.json()["job"] == "the one"

@pytest.mark.regression
def test_delete_user():
	response = client.delete("/users/2")
	assert response.status_code == 204

@pytest.mark.advanced
def test_login_success():
	payload = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
	response = client.post("/login", json=payload)
	assert response.status_code == 200
	parsed = LoginSuccessResponse(**response.json())
	assert parsed.token

@pytest.mark.advanced
def test_login_failure():
	payload = {"email": "peter@klaven"}
	response = client.post("/login", json=payload)
	assert response.status_code == 400
	parsed = LoginFailureResponse(**response.json())
	assert parsed.error == "Missing password"
