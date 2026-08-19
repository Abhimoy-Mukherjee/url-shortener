# URL Shortener API

A simple URL shortener built with FastAPI and PostgreSQL. Accepts a long URL and returns a short code that redirects to the original URL.

## Tech Stack

- Python 3.11+
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic (data validation)
- Docker (for running PostgreSQL locally)

## Project Structure

```
app/
├── main.py         # FastAPI app and route definitions
├── models.py       # SQLAlchemy ORM model (URL table)
├── schemas.py      # Pydantic request/response models
├── crud.py         # Database operations (create, lookup)
├── database.py     # DB connection, session, and settings
requirements.txt
docker-compose.yml
.env.example
```

## How It Works

- `POST /shorten` accepts a URL, generates a random 6-character short code (letters + digits) using Python's `secrets` module, checks it doesn't already exist in the database, and stores the mapping.
- `GET /{short_code}` looks up the code in the database and issues a 307 redirect to the original long URL. Returns a 404 if the code isn't found.
- URLs are validated automatically by Pydantic's `HttpUrl` type, so malformed URLs are rejected before hitting the database.

## Setup & Run Locally

**1. Clone the repo and install dependencies**

```bash
pip install -r requirements.txt
```

**2. Configure environment variables**

Copy `.env.example` to `.env` and fill in your own values:

```bash
cp .env.example .env
```

```
POSTGRES_USER=postgres_username
POSTGRES_PASSWORD=your_password
POSTGRES_DB=urlshortener
BASE_URL=http://localhost:8000
```

**3. Start PostgreSQL with Docker**

```bash
docker compose up -d
```

This spins up a Postgres 16 container on port 5432 using the credentials from `.env`.

**4. Run the API**

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`. Interactive Swagger docs are at `http://localhost:8000/docs`.

## Example Usage

**Shorten a URL**

```bash
curl -X POST http://localhost:8000/shorten \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com/some/very/long/path"}'
```

Response:

```json
{
  "short_code": "aZ3xQ1",
  "short_url": "http://localhost:8000/aZ3xQ1"
}
```

**Use the short URL**

```bash
curl -L http://localhost:8000/aZ3xQ1
```

This redirects (HTTP 307) to `https://example.com/some/very/long/path`.

## Notes

- `DATABASE_URL` in `database.py` points to `localhost:5432` since only PostgreSQL runs in Docker — the FastAPI app itself runs directly on the host during local development.
- Table creation is handled automatically on startup via `Base.metadata.create_all(bind=engine)`; no separate migration step is needed for this scope.