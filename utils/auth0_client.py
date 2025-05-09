import os
import requests
import logging
from dotenv import load_dotenv

class Auth0Client:
	def __init__(self):
		load_dotenv(dotenv_path="config/.env")
		self.client_id = os.getenv("AUTH0_CLIENT_ID")
		self.client_secret = os.getenv("AUTH0_CLIENT_SECRET")
		self.token_url = os.getenv("AUTH0_TOKEN_URL")
		self.audience = os.getenv("AUTH0_AUDIENCE")
		self.secured_api_url = os.getenv("AUTH0_SECURED_API_URL")

		self.access_token = None

		self._validate_env_vars()

	def _validate_env_vars(self):
		missing = [var for var in [
			self.client_id, self.client_secret,
			self.token_url, self.audience,
			self.secured_api_url
		] if not var]
		for var in [
			self.client_id, self.client_secret,
			self.token_url, self.audience,
			self.secured_api_url
		]:
			if not var:
				print(var + " is missing")

		if missing:
			raise EnvironmentError("Missing one or more Auth0 environment variables.")

	def fetch_token(self):
		payload = {
			"grant_type": "client_credentials",
			"client_id": self.client_id,
			"client_secret": self.client_secret,
			"audience": self.audience
		}
		headers = {"Content-Type": "application/json"}

		response = requests.post(self.token_url, json=payload, headers=headers)
		if response.status_code != 200:
			logging.error(f"Failed to fetch token: {response.status_code} - {response.text}")
			raise Exception("Unable to fetch access token from Auth0.")

		self.access_token = response.json().get("access_token")
		return self.access_token

	def get(self, endpoint=""):
		if not self.access_token:
			self.fetch_token()

		url = self.secured_api_url.rstrip("/") + "/" + endpoint.lstrip("/")
		headers = {
			"Authorization": f"Bearer {self.access_token}"
		}

		response = requests.get(url, headers=headers)
		response.raise_for_status()
		return response.json()

	def post(self, endpoint="", data=None):
		if not self.access_token:
			self.fetch_token()

		url = self.secured_api_url.rstrip("/") + "/" + endpoint.lstrip("/")
		headers = {
			"Authorization": f"Bearer {self.access_token}",
			"Content-Type": "application/json"
		}

		response = requests.post(url, headers=headers, json=data or {})
		response.raise_for_status()
		return response.json()
