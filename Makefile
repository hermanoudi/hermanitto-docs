# Variáveis
PYTHON = python3
APP_NAME = hermanitto_docs_api
DOCKER_COMPOSE = sudo docker-compose

# Comandos Docker
.PHONY: up
up:
	$(DOCKER_COMPOSE) up

.PHONY: up-build
up-build:
	$(DOCKER_COMPOSE) up --build

.PHONY: down
down:
	$(DOCKER_COMPOSE) down

# Comandos de desenvolvimento
.PHONY: install
install:
	pip install -e .

.PHONY: install-dev
install-dev:
	pip install -e ".[dev]"

# Comandos de teste
.PHONY: test
test:
	pytest -v

.PHONY: test-cov
test-cov:
	pytest --cov=$(APP_NAME) --cov-report=term-missing --cov-report=html

# Comandos de formatação e lint
.PHONY: format
format:
	black . --exclude "alembic/versions|build|dist|.eggs|.git|.mypy_cache|.pytest_cache|.tox|.venv|venv|env|__pycache__"

.PHONY: lint
lint:
	black --check .
	flake8 .

# Comandos de banco de dados
.PHONY: migrate
migrate:
	alembic upgrade head

.PHONY: migrate-down
migrate-down:
	alembic downgrade -1

.PHONY: migration
migration:
	@read -p "Enter migration message: " message; \
	alembic revision --autogenerate -m "$$message"

# Comandos de limpeza
.PHONY: clean
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.pyd" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type d -name "*.egg" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".coverage" -delete
	find . -type d -name "htmlcov" -exec rm -rf {} +
	find . -type d -name ".tox" -exec rm -rf {} +
	find . -type d -name "build" -exec rm -rf {} +
	find . -type d -name "dist" -exec rm -rf {} +

# Help
.PHONY: help
help:
	@echo "Available commands:"
	@echo "Docker commands:"
	@echo "  make up         - Start containers"
	@echo "  make up-build   - Start containers with build"
	@echo "  make down       - Stop containers"
	@echo ""
	@echo "Development commands:"
	@echo "  make install     - Install package"
	@echo "  make install-dev - Install package with development dependencies"
	@echo ""
	@echo "Test commands:"
	@echo "  make test      - Run tests"
	@echo "  make test-cov  - Run tests with coverage"
	@echo ""
	@echo "Format and lint commands:"
	@echo "  make format    - Format code with black"
	@echo "  make lint      - Check code format with black"
	@echo ""
	@echo "Database commands:"
	@echo "  make migrate        - Run migrations"
	@echo "  make migrate-down  - Rollback last migration"
	@echo "  make migration     - Create new migration"
	@echo ""
	@echo "Cleanup commands:"
	@echo "  make clean     - Remove Python compiled files and caches"
