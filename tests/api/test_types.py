import pytest
from httpx import AsyncClient
from hermanitto_docs_api.models.user import User
from hermanitto_docs_api.core.security import get_password_hash, create_access_token


@pytest.mark.asyncio
async def test_create_document_type(async_client: AsyncClient, db_session):
    # Create user
    user = User(
        username="testuser",
        hashed_password=get_password_hash("testpass")
    )
    db_session.add(user)
    await db_session.commit()

    # Get token
    token = create_access_token({"sub": user.username})
    headers = {"Authorization": f"Bearer {token}"}

    # Create document type
    response = await async_client.post(
        "/api/v1/types/",
        json={"name": "boleto"},
        headers=headers
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "boleto"
    assert "id" in data


@pytest.mark.asyncio
async def test_create_duplicate_document_type(async_client: AsyncClient, db_session):
    # Create user
    user = User(
        username="testuser",
        hashed_password=get_password_hash("testpass")
    )
    db_session.add(user)
    await db_session.commit()

    # Get token
    token = create_access_token({"sub": user.username})
    headers = {"Authorization": f"Bearer {token}"}

    # Create first type
    await async_client.post(
        "/api/v1/types/",
        json={"name": "boleto"},
        headers=headers
    )

    # Try to create duplicate
    response = await async_client.post(
        "/api/v1/types/",
        json={"name": "boleto"},
        headers=headers
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "Document type already exists"


@pytest.mark.asyncio
async def test_list_document_types(async_client: AsyncClient, db_session):
    # Create user
    user = User(
        username="testuser",
        hashed_password=get_password_hash("testpass")
    )
    db_session.add(user)
    await db_session.commit()

    # Get token
    token = create_access_token({"sub": user.username})
    headers = {"Authorization": f"Bearer {token}"}

    # Create multiple types
    type_names = ["boleto", "comprovante", "holerite"]
    for name in type_names:
        await async_client.post(
            "/api/v1/types/",
            json={"name": name},
            headers=headers
        )

    # List types
    response = await async_client.get("/api/v1/types/", headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert len(data) == len(type_names)
    assert all(t["name"] in type_names for t in data)


@pytest.mark.asyncio
async def test_list_types_unauthorized(async_client: AsyncClient):
    response = await async_client.get("/api/v1/types/")
    assert response.status_code == 401
    assert response.json()["detail"] == "Not authenticated"
