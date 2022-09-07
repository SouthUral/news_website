runserver:
	poetry run site_news/manage.py runserver 4000

install:
	poetry install

shell:
	poetry run site_news/manage.py shell

migrate:
	poetry run site_news/manage.py migrate
