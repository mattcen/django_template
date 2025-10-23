.PHONY: help setup dev test makemigration migrate superuser clean fixtures venv lint

#DJANGO_FIXTURES+=

help: ## Display this help message
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

venv: ## Create and activate Python virtual environment
	uv venv .venv
	@echo "Virtual environment created. To activate, run: source .venv/bin/activate"

setup: venv ## Initial setup: create venv, install dependencies and create .env
	uv pip install -r django/requirements.txt
	test -f .env || cp .env.example .env

clean: ## Clean database, migration files, and virtual environment
	find . -type f -name "*.sqlite3" -delete
	rm -rf .venv
	rm -rf __pycache__
	rm -rf .pytest_cache
	@echo "Database, migrations, and virtual environment cleaned. Run 'make setup' to recreate them."

makemigration: ## Make migrations
	uv run python ./django/manage.py makemigrations

migrate: ## Migrate database
	$(COMPOSE_PATH) uv run python ./django/manage.py migrate
	$(COMPOSE_PATH) uv run python ./django/manage.py migrate --run-syncdb

superuser: ## Create a superuser (admin@example.com)
	@echo "Creating superuser with username: root and password: root"
	DJANGO_SUPERUSER_PASSWORD=root $(COMPOSE_PATH) uv run python ./django/manage.py createsuperuser --noinput --username root --email root@example.com || true

fixtures: ## Load initial data fixtures
	$(COMPOSE_PATH) uv run python ./django/manage.py loaddata $(DJANGO_FIXTURES)

start: ## Start the server
	open http://localhost:8000/admin
	uv run python ./django/manage.py runserver

dev: setup makemigration migrate superuser fixtures start ## Set up development environment
	@echo "Development environment is ready!"

static: ## Collect static files
	uv run ./django/manage.py collectstatic --noinput

test: static ## Run tests
	uv run pytest --cov-fail-under=90 -n auto

build:
	docker compose build

check: # Check ruff linting and formatting
	uv run ruff check
	uv run ruff format --check

lint: ## Fix ruff linting and formatting
	uv run ruff check --fix
	uv run ruff format
