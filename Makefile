
mypy:
	mypy --disallow-untyped-defs src/

test:
	LOG_LEVEL=WARNING pytest --flake8 --timeout=10

run:
	uvicorn main:app
