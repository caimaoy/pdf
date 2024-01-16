.PHONY: setup test cov clean

PROJECT = xpdf
PRE_COMMIT_FILE = .git/hooks/pre-commit

install: poetry-install pre-commit-install cov

poetry-install:
	poetry install

test:
	pytest

cov:
	pytest --cov=$(PROJECT) tests/

pre-commit:
	pre-commit run --all-files

# update: pre-commit-update

# pre-commit-update:
# 	pre-commit autoupdate

pre-commit-install:
	@if [ ! -f $(PRE_COMMIT_FILE) ]; then pre-commit install; fi

clean:
	@rm -rf {.mypy_cache,.pytest_cache,.coverage}
	@rm -rf $(PROJECT)/__pycache__
	@rm -rf tests/__pycache__
