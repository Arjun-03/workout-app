# Workout Progression Tracker

A backend for a workout-tracking application aimed at serious gym-goers, with a
strong emphasis on **progression analytics** — estimated 1-rep-max trends,
personal-record detection, and volume tracking — rather than just logging sets.

> **Project status: early development.**
> This is a learning-focused, production-quality build in progress. Authentication
> is implemented and working. The core fitness features (exercises, workout logging,
> progression engine) are being built next — see the [Roadmap](#roadmap).

---

## Why this project exists

Free apps like Hevy and Strong already log workouts well, so logging alone isn't a
reason to switch. The goal here is to be the best tool for **understanding your
progression**: automatically detecting when you hit a personal record, estimating
your strength on each lift over time, and surfacing volume trends — the analytics
serious lifters care about.

This repository is also a deliberate exercise in building a backend to real
production standards (clean layering, migrations, secure auth, tests), not a
throwaway tutorial project.

---

## Tech stack

**Currently used**

- **Python 3.12+**
- **FastAPI** — web framework (REST API)
- **PostgreSQL** — database, run via Docker
- **SQLAlchemy** — ORM (Python objects mapped to database tables)
- **Alembic** — database migrations (versioned schema changes)
- **Pydantic** — request/response validation
- **JWT (PyJWT)** — token-based authentication
- **Argon2 (pwdlib)** — password hashing
- **Docker / Docker Compose** — runs the PostgreSQL database

**Planned (not yet used)**

Redis (caching), Celery (background jobs), Sentry (error monitoring),
GitHub Actions (CI/CD), and a web frontend. These are intentionally deferred until
the features that need them exist.

---

## What works today

- User registration (`POST /api/v1/auth/register`) with securely hashed passwords
- Login (`POST /api/v1/auth/login`) returning a JWT access token
- A protected endpoint (`GET /api/v1/users/me`) that requires a valid token
- Automatic, interactive API docs at `/docs`

---

## Getting started

### Prerequisites

- [Python 3.12+](https://www.python.org/downloads/)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) (running)
- [Git](https://git-scm.com/)

### 1. Clone and enter the project

```bash
git clone https://github.com/Arjun-03/workout-app.git
cd workout-app
```

### 2. Start the database

From the project root:

```bash
docker compose up -d
```

This starts PostgreSQL in a container.

### 3. Set up the backend

```bash
cd backend
python -m venv .venv
```

Activate the virtual environment:

- **Windows (PowerShell):** `.\.venv\Scripts\Activate.ps1`
- **macOS / Linux:** `source .venv/bin/activate`

Install dependencies:

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Copy the example file and fill in your own values:

```bash
cp .env.example .env
```

Then open `.env` and set:

- `DATABASE_URL` — connection string for the local database
- `SECRET_KEY` — a strong random value (generate one with:
  `python -c "import secrets; print(secrets.token_hex(32))"`)
- `ACCESS_TOKEN_EXPIRE_MINUTES` — e.g. `30`

### 5. Apply database migrations

```bash
alembic upgrade head
```

This creates the database tables.

### 6. Run the app

```bash
fastapi dev app/main.py
```

The API is now at **http://127.0.0.1:8000**, and the interactive docs are at
**http://127.0.0.1:8000/docs**.

---

## Project structure

The backend follows a layered ("clean") architecture — each layer has one job and
talks only to its neighbours:

```
backend/
├── app/
│   ├── main.py            # Application entry point; wires routers together
│   ├── core/              # Foundations: config, database connection, security
│   ├── models/            # SQLAlchemy models (database table definitions)
│   ├── schemas/           # Pydantic schemas (API request/response shapes)
│   ├── api/               # Routes — receive HTTP requests, return responses
│   │   └── v1/            # Versioned endpoints (/api/v1/...)
│   ├── services/          # Business logic and rules
│   └── repositories/      # The only code that talks to the database
├── alembic/               # Migration history
├── docker-compose.yml     # (at repo root) PostgreSQL service
├── Dockerfile             # (planned)
└── requirements.txt       # Python dependencies
```

**Request flow:** an HTTP request enters through `api/` → business rules run in
`services/` → database access happens in `repositories/` → the response is filtered
through a `schemas/` model on the way out.

---

## Roadmap

- [x] **Phase 0** — Project setup, Docker, database, migrations
- [x] **Phase 1** — Authentication (register, login, protected routes)
- [ ] **Phase 2** — Exercise database and workout logging
- [ ] **Phase 3** — Progression engine (estimated 1RM, volume, PR detection)
- [ ] **Phase 4** — Analytics endpoints and charts
- [ ] **Phase 5** — Deployment, monitoring, and CI/CD
- [ ] **Phase 6** — Web frontend, then subscriptions

---

## License

Not yet licensed. All rights reserved for now.
