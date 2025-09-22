from hermanitto_docs_api.models.document_type import DocumentType
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from hermanitto_docs_api.schemas.document_type_schema import DocumentTypeCreate
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status


async def create_type(db: AsyncSession, type_in: DocumentTypeCreate):
    doc_type = DocumentType(name=type_in.name)
    db.add(doc_type)
    try:
        await db.commit()
        await db.refresh(doc_type)
        return doc_type
    except IntegrityError:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Type already exists",
        )


async def list_types(db: AsyncSession):
    result = await db.execute(select(DocumentType))
    return result.scalars().all()
