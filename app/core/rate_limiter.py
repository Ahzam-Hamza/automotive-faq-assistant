import time
from collections import defaultdict


class RateLimiter:
    def __init__(self, max_requests: int = 5, window_seconds: int = 10):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.requests = defaultdict(list)

    def allow_request(self, client_ip: str) -> bool:
        current_time = time.time()

        # Remove expired timestamps
        self.requests[client_ip] = [
            timestamp
            for timestamp in self.requests[client_ip]
            if current_time - timestamp < self.window_seconds
        ]

        # Check if limit exceeded
        if len(self.requests[client_ip]) >= self.max_requests:
            return False

        # Record this request
        self.requests[client_ip].append(current_time)
        return True
