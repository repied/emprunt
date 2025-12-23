.PHONY: install run dev test

install:
	python -m pip install --upgrade pip
	pip install -r requirements.txt
	python -m pip install -e .

dev:
	uvicorn emprunt.app:app --reload --host 0.0.0.0 --port 8000

test:
	pytest -q
