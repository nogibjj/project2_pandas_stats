install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
format:
	black src/*.py

lint:
	pylint --disable=R,C --ignore-patterns=src/test_.*?py src/*.py

test:
	python3 -m pytest -vv --cov=main src/test_*.py

all: install format lint test