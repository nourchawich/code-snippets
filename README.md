# code-snippets

## Setup

1. Clone repo
1. Install and activate virtual environment using [Pipenv](https://pipenv.readthedocs.io/en/latest/)
    ```bash
    pipenv install
    pipenv shell
    ```
1. Clone `.env.example` and rename it to `.env`
    ```bash
    cp .env.example .env
    ```
    > You might need to modify `DATABASE_URL` to match your PostgresSQL database credentials
    > For new setup, create new database using `createdb snippets`
    > This requires a working PostgresSQL server installation and its binaries to be available under $PATH
1. Run migrations
    ```bash
    python manage.py migrate
    ```
1. Collect static files (not necessary on development i.e. when DEBUG = True)
    ```bash
    python manage.py collectstatic
    ```
1. Run development server
    ```bash
    python manage.py runserver
    ```
