"""
Simple in-memory cache system.
"""

from typing import Any
from datetime import datetime, timedelta


class SimpleCache:
    def __init__(self, ttl_seconds: int = 300):
        self.store = {}
        self.ttl = ttl_seconds

    def get(self, key: str) -> Any:
        if key in self.store:
            value, expiry = self.store[key]

            if datetime.utcnow() < expiry:
                return value

            # expired → remove
            del self.store[key]

        return None

    def set(self, key: str, value: Any):
        expiry = datetime.utcnow() + timedelta(seconds=self.ttl)
        self.store[key] = (value, expiry)
