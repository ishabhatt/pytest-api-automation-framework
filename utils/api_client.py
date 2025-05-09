import requests
import os
from typing import Optional, Dict
from dotenv import load_dotenv

load_dotenv(dotenv_path="config/.env")
BASE_URL = os.getenv("BASE_URL")
API_KEY = os.getenv("API_KEY")

DEFAULT_HEADERS = {
	"Content-Type": "application/json",
	"X-API-Key": API_KEY  
}

class APIClient:
	def __init__(self, base_url : str= BASE_URL):
		self.base_url = base_url

	def get(self, endpoint: str, headers: Optional[Dict] = None, params: Optional[Dict] = None):
		headers = headers or DEFAULT_HEADERS
		return requests.get(f"{self.base_url}{endpoint}", headers=headers, params=params)

	def post(self, endpoint: str, headers: Optional[Dict] = None, json: Optional[Dict] = None):
		headers = headers or DEFAULT_HEADERS
		return requests.post(f"{self.base_url}{endpoint}", headers=headers, json=json)

	def put(self, endpoint: str, headers: Optional[Dict] = None, json: Optional[Dict] = None):
		headers = headers or DEFAULT_HEADERS
		return requests.put(f"{self.base_url}{endpoint}", headers=headers, json=json)

	def delete(self, endpoint: str, headers: Optional[Dict] = None):
		headers = headers or DEFAULT_HEADERS
		return requests.delete(f"{self.base_url}{endpoint}", headers=headers)
