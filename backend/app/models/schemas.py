"""
Pydantic Request & Response Schemas
=====================================
Owner: Ritik Budhathoki

Defines validation schemas for all API request bodies and responses.
FastAPI uses these for auto-validation and Swagger UI documentation.

TODO (Ritik):
    - Define UserRegisterRequest
    - Define UserLoginRequest
    - Define TokenResponse
    - Define DiagnosisResponse (disease_name, confidence, treatment)
    - Define TreatmentResponse
    - Define HealthResponse
    - Define ErrorResponse
"""

from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime


class UserRegisterRequest(BaseModel):
    """Request schema for user registration."""
    # TODO (Ritik): Add username, email, password fields with validation
    pass


class UserLoginRequest(BaseModel):
    """Request schema for user login."""
    # TODO (Ritik): Add username, password fields
    pass


class TokenResponse(BaseModel):
    """Response schema for authentication tokens."""
    # TODO (Ritik): Add access_token, refresh_token, token_type, expires_in
    pass


class TreatmentDetail(BaseModel):
    """Nested schema for treatment information."""
    # TODO (Ritik): Add chemical_control, cultural_control, preventive_measures, safety_note, source
    pass


class DiagnosisResponse(BaseModel):
    """
    Response schema for POST /diagnose.

    Returned after successful disease classification and treatment lookup.

    TODO (Ritik):
        - Add: disease_name, confidence (float 0-1), crop, disease_class,
               is_healthy, treatment (TreatmentDetail), inference_time_ms, timestamp
    """
    pass


class HealthResponse(BaseModel):
    """Response schema for GET /health."""
    # TODO (Ritik): Add status, version, model_loaded, database_connected
    pass
