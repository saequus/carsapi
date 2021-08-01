shell:
		poetry shell

install:
		poetry install

format:
		black .
		isort --only-modified .

lint:
		black --check .
		isort  --check-only --only-modified .

start:
		python3 manage.py runserver

migrate:
		python3 manage.py migrate

up:
	docker-compose up

test:
		python3 manage.py test .

tox:
		tox

