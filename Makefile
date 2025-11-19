.PHONY: help install test lint format type-check check-all clean

help:
	@echo "Available commands:"
	@echo "  make install     - Install the project in editable mode with dev dependencies"
	@echo "  make test        - Run all tests with pytest"
	@echo "  make lint        - Run ruff linter"
	@echo "  make format      - Format code with black"
	@echo "  make type-check  - Run mypy type checker"
	@echo "  make check-all   - Run all quality checks (lint, format, type-check, test)"
	@echo "  make clean       - Remove generated files and caches"

install:
	pip install -e .[dev]

test:
	pytest -v

test-cov:
	pytest -v --cov=src --cov-report=term-missing --cov-report=html

lint:
	ruff check src tests

lint-fix:
	ruff check --fix src tests

format:
	black src tests

format-check:
	black --check src tests

type-check:
	mypy src

check-all: lint format-check type-check test

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/
	rm -rf .ruff_cache/
	rm -rf htmlcov/
	rm -rf .coverage
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
