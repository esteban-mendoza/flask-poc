# Flask POC

This project is a proof of concept of a REST API in Flask, it:

- uses Marshmallow for schema validation,
- Flask-SQLAlchemy for managing data models,
- PosgreSQL as the database,
- implements authentication of fresh and non-fresh tokens with JWT,
- uses Alembic for data migrations,
- implements development and production configurations,
- uses Docker Compose for local development,
- Swagger for API documentation,
- Gunicorn as a WSGI production server.

## Get started

1. [Install Pyenv](https://github.com/pyenv/pyenv?tab=readme-ov-file#installation)
2. Clone the repository.
3. Execute the following commands:

    ```bash
    # Install the required Python version
    pyenv install 3.10.12

    # Create and activate a virtual environment
    python3 -m venv .venv
    source .venv/bin/activate

    # Install the dependencies
    pip install -r requirements.txt
    ````

4. Create a `.env` file based on the `.env.example`. The `DATABASE_URL` variable is configured for local development with Docker Compose. If running this service in production, you must provide the same environment variables.

## Run locally

This project uses Docker Compose to run the application and the database. To run the application locally:

1. Start the application:

    ```bash
    docker compose up
    ```

2. Perform database migrations:

    ```bash
    docker compose run web flask db upgrade
    ```

Depending on your port bindings, you can access the Swagger documentation at `http://localhost:{HOST_PORT}/swagger-ui/`.
