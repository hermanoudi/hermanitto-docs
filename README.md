
# hermanitto-docs-api

API para gerenciar links de arquivos PDF (comprovantes, boletos, holerites, etc) armazenados no Google Drive.

## Funcionalidades

- Autenticação JWT com registro e login de usuários
- Cadastro e listagem de tipos de documentos (boletos, comprovantes, holerites, etc.)
- Cadastro e listagem de documentos com seus links do Google Drive
- Proteção de endpoints por autenticação
- Migrations automáticas com Alembic

## Stack Tecnológica

- FastAPI (framework web assíncrono)
- SQLAlchemy (ORM) com suporte assíncrono
- PostgreSQL (banco de dados)
- Pydantic (validação de dados)
- JWT (autenticação)
- Docker e Docker Compose (containerização)
- Pytest (testes)

## Como Executar

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/hermanitto-docs-api.git
cd hermanitto-docs-api
```

2. Copie o arquivo de configuração de ambiente:
```bash
cp .env-example .env
```

3. (Opcional) Ajuste as variáveis no arquivo `.env` se necessário:
```env
DATABASE_URL=postgresql+asyncpg://user:password@db:5432/db
SECRET_KEY=supersecret
```

4. Inicie a aplicação e o banco com Docker Compose:
```bash
docker compose up --build
```

5. Em outro terminal, aplique as migrations:
```bash
docker compose exec api alembic upgrade head
```

A API estará disponível em: [http://localhost:8000](http://localhost:8000)  
Documentação Swagger: [http://localhost:8000/docs](http://localhost:8000/docs)

## Testes

Para executar os testes:
```bash
docker compose exec api pytest
```

## Desenvolvimento

1. Instale as dependências localmente (recomendado usar venv):
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

2. Para criar uma nova migration após alterar modelos:
```bash
alembic revision --autogenerate -m "descrição da mudança"
```

3. Para atualizar o banco com a nova migration:
```bash
alembic upgrade head
```

## Estrutura do Projeto

```
hermanitto_docs_api/
├── api/
│   └── v1/
│       └── endpoints/        # Rotas da API
├── core/                    # Configurações e dependências
├── models/                  # Modelos SQLAlchemy
├── schemas/                 # Schemas Pydantic
├── services/               # Lógica de negócio
└── main.py                 # Aplicação FastAPI

tests/                      # Testes
alembic/                    # Migrations
```

## Contribuindo

1. Crie uma branch para sua feature
2. Faça as alterações
3. Adicione/atualize testes
4. Envie um Pull Request

## Licença

MIT
