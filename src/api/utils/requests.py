import requests
from playwright.sync_api import sync_playwright

from src.config import API_BASE_URL


class APIClient:
    def __init__(self):
        self.base_url = API_BASE_URL
        # self.headers = {"accept": "application/json"}

    def _request_context(self):
        return sync_playwright().start().request.new_context()

    def get(self, resource_path, headers=None):
        url = f"{self.base_url}{resource_path}"
        context = self._request_context()
        response = context.get(url)
        return response

    def post(self, resource_path, data, headers=None):
        url = f"{self.base_url}{resource_path}"
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        return response.json()

