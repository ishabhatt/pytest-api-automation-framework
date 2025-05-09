import pytest
from utils.api_client import APIClient
from utils.schema_validator import CreateUserResponse

client = APIClient()

@pytest.mark.e2e
def test_user_lifecycle():
	# Step 1: Create a new user
	payload_create = {"name": "trinity", "job": "zion operator"}
	create_response = client.post("/users", json=payload_create)
	assert create_response.status_code == 201
	user = CreateUserResponse(**create_response.json())
	assert user.name == "trinity"

	# Step 2: Simulate login (static valid credentials)
	login_payload = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
	login_response = client.post("/login", json=login_payload)
	assert login_response.status_code == 200
	assert "token" in login_response.json()

	# Step 3: Update the created user
	payload_update = {"name": "trinity", "job": "the one"}
	update_response = client.put("/users/2", json=payload_update)  # using static ID due to fake API
	assert update_response.status_code == 200
	assert update_response.json()["job"] == "the one"

	# Step 4: Delete the user
	delete_response = client.delete("/users/2")
	assert delete_response.status_code == 204