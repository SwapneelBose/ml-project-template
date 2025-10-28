run:
	uvicorn src.main:app --reload

test:
	pytest -v

lint:
	ruff check .
	black --check .
	isort --check-only .

format:
	black .
	isort .

docker-run:
	docker-compose up --build
