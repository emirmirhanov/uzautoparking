up:
	@docker-compose up -d
build:
	@docker-compose up --build -d
down:
	@docker-compose down
tg-run:
	@docker-compose exec -d parking_web python main.py
superaadmin:
	@docker-compose exec parking_web python tgAdmin/manage.py createsuperuser
dump:
	@docker exec -i scraping_postgres_1 /bin/bash -c "PGPASSWORD=a123456 pg_dump --username scraping scraping" > ~/scraping/dump.sql
restore:
	@docker exec -i scraping_postgres_1 /bin/bash -c "PGPASSWORD=a123456 psql --username scraping scraping" < ~/scraping/dump.sql
