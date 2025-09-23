from fastapi import APIRouter, Depends
from hermanitto_docs_api.core.security import get_current_user
from sqlalchemy.ext.asyncio import AsyncSession
from hermanitto_docs_api.schemas.document_type_schema import (
    DocumentTypeCreate,
    DocumentTypeOut,
)
from hermanitto_docs_api.services.type_service import create_type, list_types
from hermanitto_docs_api.core.dependencies import get_db

router = APIRouter()


@router.post("/", response_model=DocumentTypeOut)
async def create_document_type(
    type_in: DocumentTypeCreate, db: AsyncSession = Depends(get_db)
):
    return await create_type(db, type_in)


@router.get("/", response_model=list[DocumentTypeOut])
async def get_types(
    db: AsyncSession = Depends(get_db), user=Depends(get_current_user)
):
    return await list_types(db)
