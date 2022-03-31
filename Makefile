up:
	@docker-compose up -d
build:
	@docker-compose up --build -d
down:
	@docker-compose down
tg-run:
	@docker-compose exec -d web python main.py
