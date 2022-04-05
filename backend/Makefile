.PHONY: deps

start:
	docker-compose up -d

stop:
	docker-compose down

testing:
	docker-compose run app python manage.py test

superuser:
	docker-compose run app python manage.py createsuperuser

docker_build:
	docker-compose build --no-cache

docker-recreate:
	docker-compose up -d --force-recreate --build