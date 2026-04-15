"""
Authentication Tests
=====================
Owner: Ritik Budhathoki

Tests for /api/v1/auth/ endpoints:
    - test_register_success
    - test_register_duplicate_username
    - test_login_success
    - test_login_invalid_credentials
    - test_refresh_token_success
    - test_refresh_token_invalid

TODO (Ritik):
    - Implement all test cases below
    - Each test should be independent (clean DB state)
    - Test both success and failure paths
"""

import pytest


class TestUserRegistration:
    """Test suite for POST /api/v1/auth/register."""

    def test_register_success(self, client):
        """
        Test successful user registration.

        TODO (Ritik):
            - POST valid user data to /auth/register
            - Assert status_code == 201
            - Assert response contains user_id
        """
        pass

    def test_register_duplicate_username(self, client):
        """
        Test that duplicate username returns 400.

        TODO (Ritik):
            - Register same username twice
            - Assert second request returns 400
        """
        pass

    def test_register_invalid_email(self, client):
        """
        Test that invalid email format returns 422.

        TODO (Ritik):
            - POST with invalid email format
            - Assert status_code == 422
        """
        pass


class TestUserLogin:
    """Test suite for POST /api/v1/auth/login."""

    def test_login_success(self, client):
        """
        Test successful login returns JWT tokens.

        TODO (Ritik):
            - Register user first
            - POST valid credentials to /auth/login
            - Assert status_code == 200
            - Assert response has access_token and refresh_token
        """
        pass

    def test_login_wrong_password(self, client):
        """
        Test wrong password returns 401.

        TODO (Ritik):
            - POST wrong password
            - Assert status_code == 401
        """
        pass

    def test_login_nonexistent_user(self, client):
        """
        Test non-existent username returns 401.

        TODO (Ritik):
            - POST non-existent username
            - Assert status_code == 401
        """
        pass
