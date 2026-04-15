"""
Secure-Plants_Diagnosis — FastAPI Application Entry Point
=========================================================
Owner: Ritik Budhathoki (Security Lead / Backend)

This module initialises the FastAPI application, registers all routers,
configures CORS, and wires up middleware (rate limiting, logging).

TODO (Ritik):
    - Register all route prefixes
    - Add startup/shutdown event handlers (load ML model on startup)
    - Configure CORS allowed origins from .env
    - Add request ID middleware for request tracing
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# from app.api.routes import auth, diagnosis, remediation, health
# from app.api.middleware import RateLimitMiddleware, LoggingMiddleware
# from app.config import settings


def create_application() -> FastAPI:
    """
    Application factory function.

    Returns:
        FastAPI: Configured FastAPI application instance.
    """
    application = FastAPI(
        title="Secure-Plants_Diagnosis API",
        description=(
            "Secure mobile backend for real-time plant disease diagnosis "
            "using DeiT Vision Transformer and deterministic treatment engine."
        ),
        version="0.1.0",
        docs_url="/docs",
        redoc_url="/redoc",
        openapi_url="/openapi.json",
    )

    # TODO (Ritik): Configure CORS from settings.ALLOWED_ORIGINS
    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Restrict in production
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # TODO (Ritik): Add rate limiting middleware
    # application.add_middleware(RateLimitMiddleware)

    # TODO (Ritik): Add request logging middleware
    # application.add_middleware(LoggingMiddleware)

    # TODO (Ritik): Include routers
    # application.include_router(health.router, prefix="/api/v1", tags=["Health"])
    # application.include_router(auth.router, prefix="/api/v1/auth", tags=["Auth"])
    # application.include_router(diagnosis.router, prefix="/api/v1", tags=["Diagnosis"])
    # application.include_router(remediation.router, prefix="/api/v1", tags=["Treatment"])

    # TODO (Ritik): Add startup event to load ML model into memory
    # @application.on_event("startup")
    # async def startup_event():
    #     load_model()

    return application


app = create_application()
