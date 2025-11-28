"""
TITAN (Threat Intelligence, Triage & Analysis Node)
---------------------------------------------------
FastAPI-based microservice for managing and enriching Indicators of Compromise (IOCs).
"""

__version__ = "0.1.0"
__author__ = "Tanner Lyon"

# Optional: Expose reusable modules for convenience imports
from .config import get_settings


# Optional (Later Enhancement)
# from fastapi import FastAPI
# from app.routes import health, auth, iocs, intel
# from app.middleware.rate_limit import RateLimitMiddleware

# def create_app() -> FastAPI:
#     app = FastAPI(title="TITAN Threat Intelligence API", version="0.1.0")
#     app.add_middleware(RateLimitMiddleware)
#     app.include_router(health.router)
#     app.include_router(auth.router, prefix="/auth")
#     app.include_router(iocs.router, prefix="/iocs")
#     app.include_router(intel.router, prefix="/intel")
#     return app
