# TaskFlow Distributed System

## Overview

TaskFlow is a distributed task management system built with FastAPI, SQLAlchemy, Celery, Redis, and PostgreSQL.  
It uses a clean architecture with separation of concerns: API layer, service layer, and repository layer.

---

## Prerequisites

- [Docker](https://www.docker.com/products/docker-desktop)
- [Docker Compose](https://docs.docker.com/compose/)

---

## How to Run

1. **Clone the repository:**
   ```sh
   git clone https://github.com/your-username/taskflow-distributed.git
   cd taskflow-distributed
   ```

2. **Build and start the distributed system:**
   ```sh
   docker-compose up --build
   ```

   This will start:
   - FastAPI API server
   - Celery worker
   - PostgreSQL database
   - Redis (for Celery broker/results)

3. **Access the API documentation:**
   - Open your browser and go to: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## Useful Endpoints

- `POST /users/` - Create a user
- `GET /users/` - Get all users
- `GET /users/{user_id}` - Get a user by ID
- `PUT /users/{user_id}` - Update a user
- `DELETE /users/{user_id}` - Delete a user

- `POST /tasks/` - Create a task
- `GET /tasks/` - Get all tasks
- `GET /tasks/{task_id}` - Get a task by ID
- `PUT /tasks/{task_id}` - Update a task
- `DELETE /tasks/{task_id}` - Delete a task

---

## Notes

- All configuration (database, redis, etc.) is handled in `docker-compose.yml`.
- Swagger UI (`/docs`) shows all available endpoints and models, including enum descriptions for status fields.

---

## Stopping the System

To stop all services, press `CTRL+C` in the terminal where Docker Compose is running, or run:
```sh
docker-compose down
```

---

## Troubleshooting

- If you encounter database errors, ensure Docker is running and ports 5432 (Postgres) and 6379 (Redis) are available.
- For code changes to take effect, restart the containers with `docker-compose up --build`.

---