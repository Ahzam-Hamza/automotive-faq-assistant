"""
Custom middlewares used in the Automotive FAQ Assistant API.
"""

import time
import logging
from fastapi import Request
from fastapi.responses import Response
from starlette.middleware.base import BaseHTTPMiddleware

logger = logging.getLogger("app.middleware")


class LoggingMiddleware(BaseHTTPMiddleware):
    """
    Logs every incoming request and its response time.
    """

    async def dispatch(self, request: Request, call_next):
        start = time.time()

        logger.info(f"{request.method} {request.url} - Request received")

        try:
            response = await call_next(request)
        except Exception as exc:
            logger.error(f"Error while processing request: {exc}")
            raise

        duration = round((time.time() - start) * 1000, 2)

        logger.info(
            f"{request.method} {request.url} "
            f"completed with {response.status_code} in {duration}ms"
        )

        return response


class SecurityHeadersMiddleware(BaseHTTPMiddleware):
    """
    Adds basic security headers to every response.
    """

    async def dispatch(self, request: Request, call_next):
        response: Response = await call_next(request)

        # Basic security protections
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["X-XSS-Protection"] = "1; mode=block"
        response.headers["Strict-Transport-Security"] = \
            "max-age=31536000; includeSubDomains"

        return response
