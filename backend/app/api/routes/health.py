"""
Health Check Endpoint
======================
Owner: Ritik Budhathoki

GET /api/v1/health — Returns system health status.
No authentication required. Used by Docker and monitoring.

TODO (Ritik):
    - Check database connectivity
    - Check model is loaded
    - Return structured health response
"""

from fastapi import APIRouter
# from app.config import settings

router = APIRouter()


@router.get("/health", tags=["Health"])
async def health_check():
    """
    Check API health status.

    Returns basic system status including version, database
    connectivity, and model load status.

    Returns:
        dict: Health status response.

    TODO (Ritik):
        - Check DB connection via try/except
        - Check if model is loaded in memory
        - Return proper HealthResponse schema
    """
    # TODO (Ritik): Replace with real checks
    return {
        "status": "healthy",
        "version": "0.1.0",
        "model_loaded": False,       # TODO: Check actual model state
        "database_connected": False, # TODO: Check actual DB state
    }
