"""
Security Utilities — JWT Authentication
========================================
Owner: Ritik Budhathoki (Security Lead)

Handles JWT token creation, decoding, and password hashing.
Used by auth routes and authentication middleware.

Security Design:
    - JWT signed with HS256 using a secret key stored in .env
    - Access tokens expire in 30 minutes
    - Refresh tokens expire in 7 days
    - Passwords hashed with bcrypt (cost factor 12)

TODO (Ritik):
    - Implement create_access_token()
    - Implement create_refresh_token()
    - Implement verify_token() — decode and validate JWT
    - Implement get_password_hash() — bcrypt hash
    - Implement verify_password() — bcrypt verify
    - Add token blacklist for logout (optional, store in Redis/DB)
"""

from datetime import datetime, timedelta
from typing import Optional

# from jose import JWTError, jwt
# from passlib.context import CryptContext
# from app.config import settings


# TODO (Ritik): Initialise bcrypt password context
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """
    Create a signed JWT access token.

    Args:
        data: Payload data to encode (e.g., {"sub": user_id}).
        expires_delta: Custom expiry duration. Defaults to settings value.

    Returns:
        str: Encoded JWT access token string.

    TODO (Ritik): Implement JWT creation using python-jose
    """
    pass


def create_refresh_token(data: dict) -> str:
    """
    Create a signed JWT refresh token (longer-lived).

    Args:
        data: Payload data to encode.

    Returns:
        str: Encoded JWT refresh token string.

    TODO (Ritik): Implement with longer expiry (JWT_REFRESH_TOKEN_EXPIRE_DAYS)
    """
    pass


def verify_token(token: str) -> Optional[dict]:
    """
    Decode and verify a JWT token.

    Args:
        token: JWT token string from Authorization header.

    Returns:
        dict: Decoded payload if valid, None if invalid/expired.

    Raises:
        HTTPException 401: If token is invalid or expired.

    TODO (Ritik): Implement token verification with JWTError handling
    """
    pass


def get_password_hash(password: str) -> str:
    """
    Hash a plain-text password using bcrypt.

    Args:
        password: Plain-text password string.

    Returns:
        str: bcrypt-hashed password string.

    TODO (Ritik): Implement using pwd_context.hash()
    """
    pass


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify a plain-text password against a bcrypt hash.

    Args:
        plain_password: Plain-text password to verify.
        hashed_password: Stored bcrypt hash from database.

    Returns:
        bool: True if password matches, False otherwise.

    TODO (Ritik): Implement using pwd_context.verify()
    """
    pass
