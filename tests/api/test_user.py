import pytest
from fastapi.testclient import TestClient
from hermanitto_docs_api.core.security import create_access_token
from hermanitto_docs_api.models.user import User
from hermanitto_docs_api.core.security import get_password_hash


@pytest.mark.asyncio
async def test_register_user(client: TestClient):
    response = client.post(
        "/api/v1/users/register",
        json={"username": "testuser", "password": "testpass"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "testuser"
    assert "id" in data
    assert "created_at" in data


@pytest.mark.asyncio
async def test_register_duplicate_user(client: TestClient):
    # First registration
    client.post(
        "/api/v1/users/register",
        json={"username": "testuser", "password": "testpass"}
    )
    
    # Try to register the same username
    response = client.post(
        "/api/v1/users/register",
        json={"username": "testuser", "password": "testpass"}
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "Username already exists"


@pytest.mark.asyncio
async def test_login_success(client: TestClient, db_session):
    # Create user
    user = User(
        username="testuser",
        hashed_password=get_password_hash("testpass")
    )
    db_session.add(user)
    await db_session.commit()

    # Try to login
    response = client.post(
        "/api/v1/users/login",
        json={"username": "testuser", "password": "testpass"}
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"


@pytest.mark.asyncio
async def test_login_invalid_credentials(client: TestClient):
    response = client.post(
        "/api/v1/users/login",
        json={"username": "wronguser", "password": "wrongpass"}
    )
    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid credentials"


@pytest.mark.asyncio
async def test_get_me(client: TestClient, db_session):
    # Create user
    user = User(
        username="testuser",
        hashed_password=get_password_hash("testpass")
    )
    db_session.add(user)
    await db_session.commit()

    # Create token
    token = create_access_token({"sub": user.username})

    # Get user details
    response = client.get(
        "/api/v1/users/me",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "testuser"


def test_get_me_invalid_token(client: TestClient):
    response = client.get(
        "/api/v1/users/me",
        headers={"Authorization": "Bearer invalid-token"}
    )
    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid token"
