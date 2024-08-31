all: up

up:
	docker-compose up --build

down:
	docker-compose down --remove-orphans

test:
	docker exec backend python3 manage.py test

shell:
	docker exec -it backend zsh

logs:
	docker-compose logs -f