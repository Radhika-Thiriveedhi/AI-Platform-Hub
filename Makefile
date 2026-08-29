.PHONY: install run test coverage compile build
install:
	python -m pip install -r requirements.txt
run:
	python run.py
test:
	python -m pytest
auto: test
coverage:
	python -m pytest --cov=. --cov-report=term-missing --cov-report=xml
compile:
	python -m compileall -q .
build:
	docker build -t ai-platform-hub .
