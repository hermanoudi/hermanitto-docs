# Documentação do Hermanitto Docs API

## Visão Geral
O Hermanitto Docs API é uma API RESTful desenvolvida para gerenciamento de documentos e tipos de documentos, com autenticação de usuários e controle de acesso. O projeto foi construído usando FastAPI, um framework moderno e de alto desempenho para Python, com suporte a operações assíncronas.

## Tecnologias Utilizadas

### Core
- **FastAPI**: Framework web assíncrono de alta performance
- **Pydantic**: Validação de dados e serialização
- **SQLAlchemy**: ORM (Object-Relational Mapping) para banco de dados
- **Alembic**: Gerenciamento de migrações de banco de dados
- **PostgreSQL**: Banco de dados principal (AsyncPG para conexões assíncronas)
- **SQLite**: Banco de dados para testes

### Segurança
- **PassLib**: Hashing de senhas
- **Python-Jose**: Implementação JWT para autenticação
- **Bcrypt**: Algoritmo de hash para senhas

### Testes
- **Pytest**: Framework de testes
- **Pytest-AsyncIO**: Suporte a testes assíncronos
- **Coverage**: Análise de cobertura de código
- **HTTPx**: Cliente HTTP para testes de integração

### Ferramentas de Desenvolvimento
- **Black**: Formatação de código
- **Flake8**: Linting
- **MyPy**: Verificação de tipos estáticos
- **iSort**: Organização de imports

## Arquitetura

### Estrutura de Diretórios
```
hermanitto_docs_api/
├── api/
│   └── v1/
│       └── endpoints/        # Rotas da API
├── core/                    # Configurações centrais
│   ├── config.py           # Configurações do app
│   ├── dependencies.py     # Dependências FastAPI
│   └── security.py         # Funções de segurança
├── models/                 # Modelos SQLAlchemy
├── schemas/                # Schemas Pydantic
└── services/              # Lógica de negócios
```

### Camadas da Aplicação
1. **API (endpoints)**: Rotas HTTP e validação de requisições
2. **Schemas**: Validação de dados e serialização
3. **Services**: Lógica de negócios
4. **Models**: Representação do banco de dados
5. **Core**: Configurações e utilitários

### Padrões de Projeto
- **Dependency Injection**: Utilizado para injeção de dependências nas rotas
- **Repository Pattern**: Abstração do acesso ao banco de dados
- **Service Layer**: Separação da lógica de negócios
- **SOLID Principles**: Princípios de design orientado a objetos

## Funcionalidades

### Usuários
- Registro de usuários
- Autenticação via JWT
- Gerenciamento de perfil

#### Exemplos de Chamadas (Usuários)

##### Registro de Usuário
```bash
curl -X POST \
  http://localhost:8000/api/v1/users/register \
  -H 'Content-Type: application/json' \
  -d '{
    "username": "usuario",
    "password": "senha123"
  }'
```

##### Autenticação (Obter Token)
```bash
curl -X POST \
  http://localhost:8000/api/v1/users/login \
  -H 'Content-Type: application/json' \
  -d '{
    "username": "usuario",
    "password": "senha123"
  }'
```
(A resposta conterá o token JWT no campo `access_token`. Utilize-o nas próximas chamadas.)

### Documentos
- CRUD de documentos
- Associação com tipos de documentos
- Metadados e versionamento

#### Exemplos de Chamadas (Documentos)

##### Criar Documento (Requer Token)
```bash
curl -X POST \
  http://localhost:8000/api/v1/documents/ \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer SEU_TOKEN_JWT' \
  -d '{
    "type_id": 1,
    "link": "https://exemplo.com/documento.pdf"
  }'
```
(Substitua `SEU_TOKEN_JWT` pelo token obtido na autenticação.)

##### Listar Documentos (Requer Token)
```bash
curl -X GET \
  http://localhost:8000/api/v1/documents/ \
  -H 'Authorization: Bearer SEU_TOKEN_JWT'
```

### Tipos de Documentos
- Gerenciamento de tipos de documentos
- Validação baseada em tipos
- Hierarquia de tipos

#### Exemplos de Chamadas (Tipos de Documentos)

##### Criar Tipo de Documento (Requer Token)
```bash
curl -X POST \
  http://localhost:8000/api/v1/types/ \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer SEU_TOKEN_JWT' \
  -d '{
    "name": "Tipo de Documento Exemplo"
  }'
```

##### Listar Tipos de Documento (Requer Token)
```bash
curl -X GET \
  http://localhost:8000/api/v1/types/ \
  -H 'Authorization: Bearer SEU_TOKEN_JWT'
```

## Testes

### Estrutura de Testes
- Testes unitários
- Testes de integração
- Fixtures reutilizáveis
- Banco de dados em memória para testes

### Cobertura
- Meta de cobertura: 90%
- Relatórios detalhados via pytest-cov
- Integração com CI/CD

## CI/CD

### GitHub Actions Pipeline
- Verificação de código (Black, Flake8, MyPy)
- Execução de testes
- Análise de cobertura
- Deploy automático (quando configurado)

## Como Executar

### Desenvolvimento Local
```bash
# Instalar dependências
make install-dev

# Configurar ambiente
cp .env-example .env

# Executar migrações
make migrate

# Iniciar servidor
make up
```

### Testes
```bash
# Executar todos os testes
make test

# Verificar cobertura
make test-cov
```

### Docker
```bash
# Build e execução
make up-build
```

## Boas Práticas

### Código
- PEP 8 para estilo de código
- Type hints em todas as funções
- Docstrings para documentação
- Commits semânticos

### Banco de Dados
- Migrações versionadas
- Índices otimizados
- Transações atômicas

### API
- REST compliant
- Versionamento via URL
- Documentação automática via OpenAPI
- Rate limiting

## Contribuição
1. Fork o projeto
2. Crie uma branch para sua feature
3. Execute os testes
4. Envie um Pull Request

## Próximos Passos
- [ ] Implementar cache com Redis
- [ ] Adicionar logging estruturado
- [ ] Melhorar documentação da API
- [ ] Implementar rate limiting
- [ ] Adicionar métricas e monitoramento
