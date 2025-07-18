import resms
import requests


class BaseClient:
    BASE_URL = "https://api.resms.dev"

    def __init__(self):
        if not resms.api_key:
            raise ValueError("API key not set")
        self.headers = {
            "x-api-key": resms.api_key,
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

    def get(self, path, params=None):
        url = f"{self.BASE_URL}{path}"
        resp = requests.get(url, headers=self.headers, params=params)
        resp.raise_for_status()
        return resp.json()

    def post(self, path, data=None):
        url = f"{self.BASE_URL}{path}"
        resp = requests.post(url, headers=self.headers, json=data)
        resp.raise_for_status()
        return resp.json()

    def delete(self, path, data=None):
        url = f"{self.BASE_URL}{path}"
        resp = requests.delete(url, headers=self.headers, json=data)
        resp.raise_for_status()
        return resp.json()
