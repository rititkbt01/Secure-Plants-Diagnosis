"""
API Middleware — Rate Limiting & Request Logging
=================================================
Owner: Ritik Budhathoki (Security Lead)

Middleware applied to all incoming requests:
1. Rate Limiting  — 100 requests per 60 seconds per client IP
2. Request Logging — Log request method, path, status, latency

Rate Limiting Design:
    Uses slowapi (wrapper around limits library).
    Key: client IP address from X-Forwarded-For or request.client.host
    Limit: 100/minute (configurable via .env RATE_LIMIT_REQUESTS)
    Response on exceed: HTTP 429 Too Many Requests

TODO (Ritik):
    - Configure slowapi limiter
    - Apply rate limit decorator to diagnosis endpoint
    - Implement request logging middleware
    - Log: timestamp, user_id (if authed), method, path, status, latency_ms
"""

from fastapi import Request
from fastapi.responses import JSONResponse
# from slowapi import Limiter, _rate_limit_exceeded_handler
# from slowapi.util import get_remote_address
# from slowapi.errors import RateLimitExceeded
# from app.config import settings


# TODO (Ritik): Initialize slowapi limiter
# limiter = Limiter(key_func=get_remote_address)


class RequestLoggingMiddleware:
    """
    Middleware to log every incoming request and response.

    Logs: timestamp, method, path, status_code, latency_ms, client_ip

    TODO (Ritik):
        - Implement __call__ method
        - Record start time before request
        - Log response status and latency after request
        - Use loguru logger
    """

    async def __call__(self, request: Request, call_next):
        """
        Process request and log details.

        TODO (Ritik): Implement logging logic here.
        """
        # TODO: Log request start
        response = await call_next(request)
        # TODO: Log request end (status + latency)
        return response
