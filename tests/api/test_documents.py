import pytest
from httpx import AsyncClient
from hermanitto_docs_api.models.document_type import DocumentType
from hermanitto_docs_api.models.user import User
from hermanitto_docs_api.core.security import get_password_hash, create_access_token


@pytest.mark.asyncio
async def test_create_document(async_client: AsyncClient, db_session):
    # Create user
    user = User(
        username="testuser",
        hashed_password=get_password_hash("testpass")
    )
    db_session.add(user)
    
    # Create document type
    doc_type = DocumentType(name="comprovante")
    db_session.add(doc_type)
    await db_session.commit()

    # Get token
    token = create_access_token({"sub": user.username})
    headers = {"Authorization": f"Bearer {token}"}

    # Create document
    doc_data = {
        "type_id": doc_type.id,
        "link": "https://drive.google.com/file.pdf"
    }
    response = await async_client.post(
        "/api/v1/documents/",
        json=doc_data,
        headers=headers
    )
    assert response.status_code == 200
    data = response.json()
    assert data["link"] == doc_data["link"]
    assert data["type_id"] == doc_type.id
    assert "id" in data
    assert "created_at" in data


@pytest.mark.asyncio
async def test_get_documents(async_client: AsyncClient, db_session):
    # Create user and type first
    user = User(
        username="testuser",
        hashed_password=get_password_hash("testpass")
    )
    db_session.add(user)
    
    doc_type = DocumentType(name="comprovante")
    db_session.add(doc_type)
    await db_session.commit()

    # Create multiple documents
    doc_data = [
        {"type_id": doc_type.id, "link": "https://drive.google.com/file1.pdf"},
        {"type_id": doc_type.id, "link": "https://drive.google.com/file2.pdf"}
    ]

    # Get token
    token = create_access_token({"sub": user.username})
    headers = {"Authorization": f"Bearer {token}"}

    # Create documents
    for doc in doc_data:
        await async_client.post("/api/v1/documents/", json=doc, headers=headers)

    # List documents
    response = await async_client.get("/api/v1/documents/", headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert data[0]["link"] == doc_data[0]["link"]
    assert data[1]["link"] == doc_data[1]["link"]


@pytest.mark.asyncio
async def test_create_document_invalid_type(async_client: AsyncClient, db_session):
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

    # Try to create document with invalid type
    doc_data = {
        "type_id": 9999,  # non-existent type
        "link": "https://drive.google.com/file.pdf"
    }
    response = await async_client.post(
        "/api/v1/documents/",
        json=doc_data,
        headers=headers
    )
    assert response.status_code == 404
    assert response.json()["detail"] == "Document type not found"


@pytest.mark.asyncio
async def test_get_documents_unauthorized(async_client: AsyncClient):
    response = await async_client.get("/api/v1/documents/")
    assert response.status_code == 401
    assert response.json()["detail"] == "Not authenticated"
