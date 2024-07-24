# Use an official Python runtime as a parent image - note the need for 3.12.3 due to Pydantic bug at 3.12.4
FROM python:3.12.4-slim

# Install debug tools
RUN apt-get update && apt-get install -y curl procps && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy the Poetry configuration and lock files to the container
# Note that Dockerfile expects the root directory as context !
COPY ./pyproject.toml /app/

# Install Poetry
RUN pip install --no-cache-dir poetry

# Install dependencies defined in pyproject.toml
RUN poetry install --no-root --only main

# Copy the rest of the application code to the container
# Note again this expects the root directory as context.
COPY ./chat-api /app/src

# Set the environment variable for FastAPI
ENV MODULE_NAME="src.app.main"

# Make port 3000 available to the world outside this container
EXPOSE 3000

# Run the FastAPI application using Uvicorn
CMD ["poetry", "run", "uvicorn", "src.app.main:app", "--host", "0.0.0.0", "--port", "3000"]
