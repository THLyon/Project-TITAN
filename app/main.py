from fastapi import FastAPI
from app.routes import health, auth, iocs, intel
from app.middleware.rate_limit import RateLimitMiddleware
from app.logging_config import logger

app = FastAPI(
    title='TITAN Threat Intelligence API', 
    version='0.1.0', 
    description='TITAN-Lite IOC Microservice (FastAPI + SQLModel)'
)

#Middleware
app.add_middleware(RateLimitMiddleware)

# Routers
app.include_router(health.router, tags=["health"])
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(iocs.router, prefix="/iocs", tags=["iocs"])
app.include_router(intel.router, prefix="/intel", tags=["intel"])

@app.on_event("startup")
def startup_event():
    logger.info("Titan API starting up...")

@app.on_event("shutdown")
def shutdown_event():
    logger.info("TITAN API shutting down...")


# Optional (Later enhancement): Use when using Optional section from apps/__init__.py
# from app import create_app
# app = create_app()
