# tests/test_oauth_github_stub.py
import pytest
import requests
import os
import webbrowser
from dotenv import load_dotenv

load_dotenv(dotenv_path="config/.env")

@pytest.mark.auth
def test_github_oauth_token_exchange():
	"""
	GitHub OAuth 2.0 Token Exchange with Launch

	This test automates:
	1. Opening the GitHub authorization URL in the default browser
	2. User logs in and authorizes manually
	3. User pastes the `code` back into the `.env` file
	4. Test exchanges it for an access token and fetches GitHub profile
	"""
	client_id = os.getenv("GITHUB_APP_CLIENT_ID")
	client_secret = os.getenv("GITHUB_APP_LIENT_SECRET")
	auth_code = os.getenv("GITHUB_AUTH_CODE")

	if not all([client_id, client_secret]):
		pytest.skip("Missing GitHub client_id or client_secret in .env")

	if not auth_code:
		auth_url = f"https://github.com/login/oauth/authorize?client_id={client_id}&scope=read:user"
		print(f"\n👉 Open this URL and authorize the app: {auth_url}\n")
		webbrowser.open(auth_url)
		pytest.skip("Authorization URL opened. Paste the `code` into .env as GITHUB_AUTH_CODE to continue.")

	token_url = "https://github.com/login/oauth/access_token"
	headers = {"Accept": "application/json"}
	data = {
		"client_id": client_id,
		"client_secret": client_secret,
		"code": auth_code
	}

	token_resp = requests.post(token_url, headers=headers, data=data)
	assert token_resp.status_code == 200
	access_token = token_resp.json().get("access_token")
	assert access_token is not None

	user_resp = requests.get("https://api.github.com/user", headers={"Authorization": f"Bearer {access_token}"})
	assert user_resp.status_code == 200
	assert "login" in user_resp.json()
	print("GitHub user:", user_resp.json()["login"])
