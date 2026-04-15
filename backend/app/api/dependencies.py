"""
FastAPI Dependency Injection
=============================
Owner: Ritik Budhathoki

Shared dependencies injected into route handlers via Depends().

Provides:
    - get_db()          — Database session (per request)
    - get_current_user() — Authenticated user from JWT

TODO (Ritik):
    - Implement get_db() with SQLAlchemy session management
    - Implement get_current_user() that:
        1. Extracts JWT from Authorization: Bearer <token> header
        2. Calls verify_token() from core/security.py
        3. Fetches user from DB by sub (user_id)
        4. Raises HTTP 401 if token invalid/user not found
"""

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
# from sqlalchemy.orm import Session
# from app.database.connection import SessionLocal
# from app.core.security import verify_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")


def get_db():
    """
    Provide a database session for the duration of a request.

    Yields:
        Session: SQLAlchemy database session.

    Usage:
        @router.get("/example")
        def example(db: Session = Depends(get_db)):
            ...

    TODO (Ritik):
        - Open SessionLocal()
        - Yield session
        - Close session in finally block
    """
    pass


async def get_current_user(token: str = Depends(oauth2_scheme)):
    """
    Validate JWT and return current authenticated user.

    Args:
        token: JWT Bearer token from Authorization header.

    Returns:
        User: Authenticated user ORM object.

    Raises:
        HTTPException 401: If token is missing, invalid, or expired.

    TODO (Ritik):
        - Call verify_token(token)
        - Extract user_id from token payload["sub"]
        - Query user from DB
        - Raise 401 if user not found or inactive
    """
    pass
