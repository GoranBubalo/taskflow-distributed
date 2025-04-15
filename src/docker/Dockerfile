# Use Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install PostgreSQL client for pg_isready
RUN apt-get update && apt-get install -y postgresql-client && rm -rf /var/lib/apt/lists/*

# Copy the entire src directory into the image
COPY ../.. .

# Copy dependencies and wait script
COPY src/docker/requirements.txt .
COPY src/docker/wait-for-postgres.sh .

# Install dependencies
RUN pip install -r requirements.txt

# Make wait-for-postgres.sh executable
RUN chmod +x wait-for-postgres.sh

ENV PYTHONPATH=/app/src
ENV DATABASE_URL=postgresql://user:password@postgres:5432/taskflow

# Expose port
EXPOSE 8000

# Command to run the application
CMD ["./wait-for-postgres.sh", "postgres", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]