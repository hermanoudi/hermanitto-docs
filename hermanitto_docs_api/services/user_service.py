from hermanitto_docs_api.models.user import User
from hermanitto_docs_api.core.security import (
    get_password_hash,
    verify_password,
)
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from hermanitto_docs_api.schemas.user_schema import UserCreate
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status


async def create_user(db: AsyncSession, user_in: UserCreate):
    user = User(
        username=user_in.username,
        hashed_password=get_password_hash(user_in.password),
    )
    db.add(user)
    try:
        await db.commit()
        await db.refresh(user)
        return user
    except IntegrityError:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already exists",
        )


async def authenticate_user(db: AsyncSession, username: str, password: str):
    result = await db.execute(select(User).where(User.username == username))
    user = result.scalar_one_or_none()
    if user and verify_password(password, user.hashed_password):
        return user
    return None


async def get_user_by_username(db: AsyncSession, username: str):
    result = await db.execute(select(User).where(User.username == username))
    return result.scalar_one_or_none()
