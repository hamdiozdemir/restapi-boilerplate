## Run commands through Docker Compose
docker-compose run --rm app sh -c "python manage.py runserver"


## Linting test
docker-compose run --rm app sh -c "flake8"