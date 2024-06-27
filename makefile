# Targets
all: install migrate createsuperuser start

install:
	poetry install

migrate:
	docker compose run --rm app poetry run python manage.py makemigrations
	docker compose run --rm app poetry run python manage.py migrate

createsuperuser:
	docker compose run --rm app poetry run python manage.py createsuperuser

start:
	docker compose up --build 

stop:
	docker compose down

restart:
	docker compose restart