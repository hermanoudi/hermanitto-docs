from hermanitto_docs_api.models.document import Document
from hermanitto_docs_api.models.document_type import DocumentType
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from hermanitto_docs_api.schemas.document_schema import DocumentCreate
from fastapi import HTTPException


async def create_document(db: AsyncSession, doc_in: DocumentCreate):
    # Verifica se o tipo existe
    result = await db.execute(
        select(DocumentType).where(DocumentType.id == doc_in.type_id)
    )
    doc_type = result.scalar_one_or_none()
    if not doc_type:
        raise HTTPException(status_code=404, detail="Document type not found")
    doc = Document(type_id=doc_in.type_id, link=doc_in.link)
    db.add(doc)
    await db.commit()
    await db.refresh(doc)
    return doc


async def list_documents(db: AsyncSession):
    result = await db.execute(select(Document))
    return result.scalars().all()
