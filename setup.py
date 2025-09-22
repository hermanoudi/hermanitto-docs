from setuptools import setup, find_packages

setup(
    name="hermanitto_docs_api",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "sqlalchemy",
        "alembic",
        "aiosqlite",
        "python-jose[cryptography]",
        "passlib[bcrypt]",
        "python-multipart",
        "uvicorn",
    ],
)
