build:
	docker compose build --progress=plain --no-cache

run:
	docker compose up --force-recreate

clean:
	docker compose down -v
