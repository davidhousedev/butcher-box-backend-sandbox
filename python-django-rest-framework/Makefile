
default: build run

# Update container requirements
.PHONY: build
build:
	docker build -t butcher-box-backend-poc-drf .

# Run the server
.PHONY: run
run: build
	docker run --rm -v "${PWD}/butcher_box_backend:/app" -p "5123:5123" butcher-box-backend-poc-drf

# Destroy the sqlite database used by Django
.PHONY: nuke
nuke:
	rm -f ./butcher_box_backend/db.sqlite3

.PHONY: migrations
migrations:
	docker run --rm -v "${PWD}/butcher_box_backend:/app" butcher-box-backend-poc-drf python manage.py makemigrations

.PHONY: migrate
migrate:
	docker run --rm -v "${PWD}/butcher_box_backend:/app" butcher-box-backend-poc-drf python manage.py migrate

.PHONY: clean
clean:
	rm -rf $$(find . -name __pycache__ -print)

.PHONY: superuser
superuser:
	docker run -it --rm -v "${PWD}/butcher_box_backend:/app" butcher-box-backend-poc-drf python manage.py createsuperuser \
		--username root \
		--email root@example.com

.PHONY: shell
shell:
	docker run -it --rm -v "${PWD}/butcher_box_backend:/app" butcher-box-backend-poc-drf python manage.py shell_plus --ptpython
