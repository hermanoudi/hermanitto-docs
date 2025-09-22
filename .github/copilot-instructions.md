# Copilot Instructions

Este documento descreve as boas práticas de programação e o modelo arquitetural adotado neste projeto FastAPI, servindo como referência para projetos futuros que desejem seguir o mesmo padrão.

---

## Boas Práticas de Programação

- **Organização de Pastas**  
  - Separe o código em módulos claros: `routers`, `schemas`, `models`, `database`, `security`, etc.
  - Mantenha os testes em uma pasta dedicada (`tests/`), com arquivos de teste separados por domínio.

- **Tipagem e Anotações**
  - Utilize tipagem estática sempre que possível (ex: `def func(x: int) -> str:`).
  - Use `Annotated` e `Depends` para dependências explícitas no FastAPI.

- **Padrão de Código**
  - Siga o padrão PEP8 e utilize ferramentas automáticas de lint e format (ex: [Black](https://pypi.org/project/black/)).
  - Limite o comprimento das linhas (ex: 79 caracteres).
  - Prefira aspas simples em strings.

- **Modelagem de Dados**
  - Use SQLAlchemy com dataclasses (`@mapped_as_dataclass`) para os modelos.
  - Defina enums para estados fixos (ex: `TodoState`).
  - Utilize relacionamentos explícitos (`relationship`) e configure `cascade` para remoção em cascata.

- **Schemas e Validação**
  - Utilize Pydantic para schemas de entrada e saída.
  - Separe schemas de entrada (`UserSchema`, `TodoSchema`) dos de saída (`UserPublic`, `TodoPublic`).
  - Use `ConfigDict(from_attributes=True)` para permitir conversão direta de modelos ORM para schemas.

- **Segurança**
  - Implemente autenticação JWT.
  - Separe funções para hash e verificação de senha.
  - Use dependências para proteger rotas sensíveis.

- **Tratamento de Erros**
  - Utilize exceções HTTP (`HTTPException`) com status codes apropriados.
  - Retorne mensagens de erro claras e padronizadas.

- **Testes**
  - Utilize `pytest` e `pytest-asyncio` para testes síncronos e assíncronos.
  - Use `factory-boy` para criação de objetos de teste.
  - Separe testes por domínio (ex: `test_user.py`, `test_todos.py`).
  - Utilize fixtures para setup de banco, usuários e autenticação.

- **Migrations**
  - Use Alembic para versionamento do banco de dados.
  - Mantenha scripts de migração claros e versionados.

- **Configuração**
  - Centralize configurações sensíveis em variáveis de ambiente e utilize Pydantic para carregá-las.
  - Não versionar arquivos `.env` ou segredos.

- **DevOps**
  - Utilize Docker para padronizar ambiente de execução.
  - Automatize tarefas comuns com scripts e `taskipy`.
  - Configure CI para rodar lint, testes e coverage.
---

## Modelo Arquitetural

- **API RESTful**  
  - Rotas organizadas por domínio (`/users`, `/todos`, `/auth`).
  - Utilize métodos HTTP adequados (GET, POST, PUT, PATCH, DELETE).
  - Utilize status codes HTTP corretos para cada resposta.

- **Separação de Responsabilidades**
  - **Routers**: Definem endpoints e regras de negócio.
  - **Schemas**: Definem contratos de entrada/saída.
  - **Models**: Representam entidades do banco de dados.
  - **Security**: Centraliza autenticação e autorização.
  - **Database**: Gerencia conexão e sessão com o banco.

- **Assincronismo**
  - Utilize SQLAlchemy assíncrono e rotas assíncronas para melhor performance.

- **Injeção de Dependências**
  - Use `Depends` para injetar sessão de banco, usuário autenticado, etc.

- **Paginação e Filtros**
  - Implemente filtros e paginação via query params em endpoints de listagem.

---

## Exemplo de Estilo de Código

```python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi_zero.models import User
from fastapi_zero.schemas import UserSchema, UserPublic
from fastapi_zero.security import get_password_hash

router = APIRouter(prefix='/users', tags=['users'])

@router.post('/', response_model=UserPublic)
async def create_user(user: UserSchema, session: AsyncSession = Depends()):
    # ... lógica de criação ...
    pass
```

# Ferramentas e Configuração
- Lint/Format: Black
- Testes: pytest, pytest-asyncio, factory-boy, freezegun
- Migrations: Alembic
- DevOps: Docker, Compose, GitHub Actions, Taskipy

## Observações
- Sempre escreva testes para novas funcionalidades.
- Prefira funções puras e side-effects controlados.
- Documente endpoints e regras de negócio relevantes.


