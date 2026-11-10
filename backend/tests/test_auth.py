"""LIFEOS — Authentication API tests."""

import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_health_check(client: AsyncClient):
    """Health endpoint should return healthy."""
    resp = await client.get("/api/v1/health")
    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "healthy"


@pytest.mark.asyncio
async def test_system_status(client: AsyncClient):
    """Status endpoint should return running."""
    resp = await client.get("/api/v1/status")
    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "running"
    assert "integrations" in data


@pytest.mark.asyncio
async def test_register_user(client: AsyncClient):
    """Should register a new user successfully."""
    resp = await client.post(
        "/api/v1/auth/register",
        json={
            "email": "test@example.com",
            "username": "testuser",
            "password": "TestPass1",
            "full_name": "Test User",
        },
    )
    assert resp.status_code == 201
    data = resp.json()
    assert data["email"] == "test@example.com"
    assert data["username"] == "testuser"
    assert data["full_name"] == "Test User"
    assert "id" in data


@pytest.mark.asyncio
async def test_register_duplicate_email(client: AsyncClient):
    """Should reject duplicate email."""
    payload = {
        "email": "dup@example.com",
        "username": "user1",
        "password": "TestPass1",
    }
    resp = await client.post("/api/v1/auth/register", json=payload)
    assert resp.status_code == 201

    payload["username"] = "user2"
    resp = await client.post("/api/v1/auth/register", json=payload)
    assert resp.status_code == 409


@pytest.mark.asyncio
async def test_register_weak_password(client: AsyncClient):
    """Should reject weak passwords."""
    resp = await client.post(
        "/api/v1/auth/register",
        json={
            "email": "weak@example.com",
            "username": "weakuser",
            "password": "tooshort",
        },
    )
    assert resp.status_code == 422


@pytest.mark.asyncio
async def test_login_success(client: AsyncClient):
    """Should login with correct credentials."""
    # Register
    await client.post(
        "/api/v1/auth/register",
        json={
            "email": "login@example.com",
            "username": "loginuser",
            "password": "TestPass1",
        },
    )

    # Login
    resp = await client.post(
        "/api/v1/auth/login",
        json={"email": "login@example.com", "password": "TestPass1"},
    )
    assert resp.status_code == 200
    data = resp.json()
    assert "access_token" in data
    assert "refresh_token" in data
    assert data["token_type"] == "bearer"


@pytest.mark.asyncio
async def test_login_wrong_password(client: AsyncClient):
    """Should reject wrong password."""
    await client.post(
        "/api/v1/auth/register",
        json={
            "email": "wrong@example.com",
            "username": "wronguser",
            "password": "TestPass1",
        },
    )

    resp = await client.post(
        "/api/v1/auth/login",
        json={"email": "wrong@example.com", "password": "WrongPass1"},
    )
    assert resp.status_code == 401


@pytest.mark.asyncio
async def test_get_current_user(client: AsyncClient):
    """Should return current user profile with valid token."""
    # Register and login
    await client.post(
        "/api/v1/auth/register",
        json={
            "email": "me@example.com",
            "username": "meuser",
            "password": "TestPass1",
        },
    )
    login_resp = await client.post(
        "/api/v1/auth/login",
        json={"email": "me@example.com", "password": "TestPass1"},
    )
    token = login_resp.json()["access_token"]

    # Get profile
    resp = await client.get(
        "/api/v1/auth/me",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert resp.status_code == 200
    data = resp.json()
    assert data["email"] == "me@example.com"
    assert data["username"] == "meuser"


@pytest.mark.asyncio
async def test_get_me_no_token(client: AsyncClient):
    """Should reject unauthenticated request."""
    resp = await client.get("/api/v1/auth/me")
    assert resp.status_code in (401, 422)


@pytest.mark.asyncio
async def test_refresh_token(client: AsyncClient):
    """Should refresh tokens."""
    # Register and login
    await client.post(
        "/api/v1/auth/register",
        json={
            "email": "refresh@example.com",
            "username": "refreshuser",
            "password": "TestPass1",
        },
    )
    login_resp = await client.post(
        "/api/v1/auth/login",
        json={"email": "refresh@example.com", "password": "TestPass1"},
    )
    refresh_token = login_resp.json()["refresh_token"]

    # Refresh
    resp = await client.post(
        "/api/v1/auth/refresh",
        json={"refresh_token": refresh_token},
    )
    assert resp.status_code == 200
    data = resp.json()
    assert "access_token" in data
    assert "refresh_token" in data


@pytest.mark.asyncio
async def test_update_profile(client: AsyncClient):
    """Should update user profile."""
    # Register and login
    await client.post(
        "/api/v1/auth/register",
        json={
            "email": "update@example.com",
            "username": "updateuser",
            "password": "TestPass1",
        },
    )
    login_resp = await client.post(
        "/api/v1/auth/login",
        json={"email": "update@example.com", "password": "TestPass1"},
    )
    token = login_resp.json()["access_token"]

    # Update
    resp = await client.patch(
        "/api/v1/auth/me",
        headers={"Authorization": f"Bearer {token}"},
        json={"full_name": "Updated Name", "timezone": "US/Eastern"},
    )
    assert resp.status_code == 200
    data = resp.json()
    assert data["full_name"] == "Updated Name"
    assert data["timezone"] == "US/Eastern"

