"""
Test Configuration and Fixtures
=================================
Owner: Ritik Budhathoki

Shared pytest fixtures for backend tests.
Sets up test database, test client, and authenticated user.

TODO (Ritik):
    - Create test database fixture (separate from production DB)
    - Create test_client fixture using FastAPI TestClient
    - Create authenticated_client fixture (with valid JWT)
    - Create sample_image fixture (test JPEG bytes)
"""

import pytest
# from fastapi.testclient import TestClient
# from app.main import app


# TODO (Ritik): Define fixtures below

# @pytest.fixture
# def client():
#     return TestClient(app)

# @pytest.fixture
# def auth_headers(client):
#     # Register + login to get JWT
#     response = client.post("/api/v1/auth/login", ...)
#     token = response.json()["access_token"]
#     return {"Authorization": f"Bearer {token}"}

# @pytest.fixture
# def sample_jpeg_bytes():
#     # Load a small test JPEG image
#     with open("tests/fixtures/sample_leaf.jpg", "rb") as f:
#         return f.read()
