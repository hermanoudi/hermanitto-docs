from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from hermanitto_docs_api.schemas.document_schema import DocumentCreate, DocumentOut
from hermanitto_docs_api.services.document_service import create_document, list_documents
from hermanitto_docs_api.core.dependencies import get_db
from hermanitto_docs_api.core.security import get_current_user

router = APIRouter()

@router.post('/', response_model=DocumentOut)
async def create_doc(doc_in: DocumentCreate, db: AsyncSession = Depends(get_db), user=Depends(get_current_user)):
    return await create_document(db, doc_in)

@router.get('/', response_model=list[DocumentOut])
async def get_docs(db: AsyncSession = Depends(get_db), user=Depends(get_current_user)):
    return await list_documents(db)
