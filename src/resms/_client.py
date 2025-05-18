from __future__ import annotations
import requests
from dataclasses import dataclass
from typing import Literal

BASE_URL = "https://api.resms.dev/"


class ReSMSError(Exception):
    """Raised on non-2xx HTTP responses."""


@dataclass(slots=True, frozen=True)
class SendResult:
    id: str
    status: Literal["queued", "sent", "failed"]


class ReSMS:
    """Tiny synchronous client around the ReSMS REST API."""

    def __init__(self, api_key: str, *, timeout: float = 10):
        if not api_key:
            raise ValueError("api_key is required")
        self._api_key = api_key
        self._timeout = timeout

    def send(self, *, to: str, message: str) -> SendResult:
        resp = requests.post(
            f"{BASE_URL}/sms/send",
            json={"to": to, "message": message},
            headers={"x-api-key": self._api_key},
            timeout=self._timeout,
        )

        if not resp.ok:
            raise ReSMSError(f"{resp.status_code} {resp.text}")

        data = resp.json()
        return SendResult(id=data["id"], status=data["status"])