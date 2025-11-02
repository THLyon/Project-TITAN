import time
from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
from app.config import get_settings

class TokenBucket: 
    def __init__(self, rate_per_minute: int): 
        self.rate = rate_per_minute / 60
        self.capacity = rate_per_minute
        self.tokens = self.capacity
        self.timestamp = time.monotonic()

    def allow(self) -> bool: 
        now = time.monotonic()
        elapsed = now - self.timestamp
        self.timestamp = now
        self.tokens = min(self.capacity, self.tokens + elapsed * self.rate)
        if self.tokens >= 1:
            self.tokens -= 1
            return True
        return False
    
class RateLimitMiddleware(BaseHTTPMiddleware): 
    def __init__(self, app):
        super().__init__(app)
        settings = get_settings()
        self.rate = settings.rate_limit_per_minute
        self.buckets = {}

    async def dispatch(self, request: Request, call_next):
        ip = request.client.host if request.client else "unknown"
        bucket = self.buckets.setdefault(ip, TokenBucket(self.rate))
        if not bucket.allow():
            return Response("Too Many Requests", status_code=429)
        return await call_next(request)