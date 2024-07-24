SHELL := /bin/bash
export PYTHONPATH := .

PYTHON_VERSION=3.12

DOCKER_IMAGE_NAME_1=restaurant-api
DOCKER_TAG_1=latest

DOCKER_IMAGE_NAME_2=chat-api
DOCKER_TAG_2=latest

DOCKER_IMAGE_NAME_3=chat-ui
DOCKER_TAG_3=latest

jupyter:
	@echo "Starting Jupyter Lab"
	poetry run jupyter lab


# Target to run the Backend (Restaurant) API
backend-serve:
	@echo "Running the Backend (Restaurant) FastAPI APIs"
	cd restaurant-api && poetry run uvicorn src.app.main:app --port 8000 --host 0.0.0.0 --reload && cd ..


# Target to build & run the docker container for the Backend (Restaurant) API
backend-build:
	@echo "Building docker image for backend API..."
	docker build -f restaurant-api/Dockerfile -t $(DOCKER_IMAGE_NAME_1) .

backend-run:
	@echo "Building docker image for backend API..."
	docker run -d -p 8000:8000 --name $(DOCKER_IMAGE_NAME_1) $(DOCKER_IMAGE_NAME_1):$(DOCKER_TAG_1)


# Target to run the Chat APIs
chat-serve:
	@echo "Running the Chat FastAPI APIs"
	cd chat-api && poetry run uvicorn app.main:app --port 3000 --host 0.0.0.0 --reload && cd ..


# Target to build and run the Docker container for the Chat API
chat-build:
	@echo "Building Docker image..."
	docker build -t $(DOCKER_IMAGE_NAME_2):$(DOCKER_TAG_2) -f chat-api/Dockerfile .

update-lockfile:
	@echo "Updating poetry.lock file..."
	poetry lock --no-update

chat-rebuild: update-lockfile chat-build
	@echo "Poetry lock file updated and Docker image built successfully."

chat-run:
	@echo "Running Docker container for Chat API..."
	docker run -d -p 3000:3000 --env-file .env --name $(DOCKER_IMAGE_NAME_2) $(DOCKER_IMAGE_NAME_2):$(DOCKER_TAG_2)


# Target to install the dependencies and run the Chat APIs
ui-install:
	@echo "Installing NPM dependencies for Chat UI"
	cd chat-ui && npm install && cd ..

ui-serve:
	@echo "Running Chat UI"
	cd chat-ui && npm run dev && cd ..


ui-build:
	@echo "Building Docker image for Chat UI frontend..."
	cd chat-ui && docker build -t $(DOCKER_IMAGE_NAME_3):$(DOCKER_TAG_3) . && cd ..

ui-run :
	@echo "Running Docker container for Chat UI frontend..."
	docker run -d -p 8080:80 --env-file .env --name $(DOCKER_IMAGE_NAME_3) $(DOCKER_IMAGE_NAME_3):$(DOCKER_TAG_3)


# Clean target to remove the Docker container
docker-clean:
	@echo "Stopping and removing Docker containers..."
	docker stop $(DOCKER_IMAGE_NAME_2) || true
	docker stop $(DOCKER_IMAGE_NAME_1) || true
	docker rm $(DOCKER_IMAGE_NAME_2) || true
	docker rm $(DOCKER_IMAGE_NAME_1) || true
	docker stop $(DOCKER_IMAGE_NAME_3) || true
	docker rm $(DOCKER_IMAGE_NAME_3) || true