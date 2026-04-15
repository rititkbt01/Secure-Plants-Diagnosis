"""
Authentication Routes
======================
Owner: Ritik Budhathoki (Security Lead)

Handles user registration, login, and token refresh.

Endpoints:
    POST /api/v1/auth/register — Register new user
    POST /api/v1/auth/login    — Login, receive JWT tokens
    POST /api/v1/auth/refresh  — Refresh access token

Security:
    - Passwords hashed with bcrypt before storage
    - JWT access token (30 min) + refresh token (7 days) issued on login
    - Rate limited (applied by middleware)

TODO (Ritik):
    - Implement register endpoint — hash password, save to DB
    - Implement login endpoint — verify password, issue JWT
    - Implement refresh endpoint — verify refresh token, issue new access token
    - Add input validation via Pydantic schemas
"""

from fastapi import APIRouter, Depends, HTTPException, status
# from app.models.schemas import UserRegisterRequest, UserLoginRequest, TokenResponse
# from app.services.auth_service import register_user, authenticate_user
# from app.core.security import create_access_token, create_refresh_token

router = APIRouter()


@router.post("/register", status_code=status.HTTP_201_CREATED, tags=["Auth"])
async def register(
    # request: UserRegisterRequest,
    # db: Session = Depends(get_db),
):
    """
    Register a new user account.

    Args:
        request: UserRegisterRequest containing username, email, password.

    Returns:
        dict: Success message and user_id.

    Raises:
        HTTPException 400: If username or email already exists.

    TODO (Ritik):
        - Validate request via Pydantic schema
        - Check if username/email already exists in DB
        - Hash password with bcrypt
        - Insert user into users table
        - Return success response
    """
    pass


@router.post("/login", tags=["Auth"])
async def login(
    # request: UserLoginRequest,
    # db: Session = Depends(get_db),
):
    """
    Authenticate user and issue JWT tokens.

    Args:
        request: UserLoginRequest containing username, password.

    Returns:
        TokenResponse: access_token, refresh_token, token_type, expires_in.

    Raises:
        HTTPException 401: If credentials are invalid.

    TODO (Ritik):
        - Fetch user from DB by username
        - Verify password with bcrypt
        - Create access + refresh JWT tokens
        - Return TokenResponse
    """
    pass


@router.post("/refresh", tags=["Auth"])
async def refresh_token(
    # request: RefreshTokenRequest,
):
    """
    Issue a new access token using a valid refresh token.

    Args:
        request: RefreshTokenRequest containing refresh_token.

    Returns:
        dict: New access_token and token_type.

    Raises:
        HTTPException 401: If refresh token is invalid or expired.

    TODO (Ritik):
        - Verify refresh token signature and expiry
        - Issue new access token
        - Return new token
    """
    pass
