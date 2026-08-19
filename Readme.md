# URL Shortener API

A simple URL shortener built with FastAPI and PostgreSQL.

## Tech Stack

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Docker

## Features

- Shorten long URLs
- Redirect short URLs to the original URL
- URL validation
- Swagger API documentation

## Run Locally

```bash
pip install -r requirements.txt
docker compose up -d
uvicorn app.main:app --reload