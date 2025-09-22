from hermanitto_docs_api.models.document import Document
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from hermanitto_docs_api.schemas.document_schema import DocumentCreate

async def create_document(db: AsyncSession, doc_in: DocumentCreate):
    doc = Document(type_id=doc_in.type_id, link=doc_in.link)
    db.add(doc)
    await db.commit()
    await db.refresh(doc)
    return doc

async def list_documents(db: AsyncSession):
    result = await db.execute(select(Document))
    return result.scalars().all()
