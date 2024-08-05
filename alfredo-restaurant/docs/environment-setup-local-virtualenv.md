# Environment setup using Poetry and local environment 

NB: This could be potentially the most challenging setup (if you don't have or are unfamiliar with WSL, Poetry, etc) or 
the quickest & most flexible (if you're comfortable with bash, `make` commands & have the necessary requirements).


## Requirements 

Please ensure your development environment has the following: 

- [Python](https://www.python.org/downloads/) (versions 3.10, 3.11 and 3.12)
- [Poetry](https://python-poetry.org/) for Python dependency management. 
- The ability to run Make commands
- Linux (WSL) if working on Windows.  Mac OSX should work out-the-box.
- Docker (optional) including docker-compose 
- node (optional) for running chat UI frontend

You may wish to consider [running with devcontainers](environment-setup-devcontainer.md) 
if you do not have the above requirements. 

<br>

## Installation & configuration  

### Install dependencies 

Install all Python dependencies with this:

```bash 
poetry self update        # Ensure you have the latest version 
poetry install 
```

This also creates a virtualenv within the `.venv` folder.   There is no need to activate this virtualenv, since we 
will execute commands using `poetry run ...` instead (which automatically runs the commands within the virtualenv, and 
also loads environment variables). 

### Configuration 

Create a `.env` file based on the sample [.env.sample](../.env.sample).

```bash 
AZURE_OPENAI_API_KEY=****************************
AZURE_OPENAI_DEPLOYMENT=gpt-4-32k
AZURE_OPENAI_API_VERSION=2024-05-01-preview
AZURE_OPENAI_ENDPOINT=https://*******.openai.azure.com/

TIMEZONE=Europe/Berlin
VITE_CHAT_API="http://127.0.0.1:3000"

```
<br>

## Running APIs locally: 

You have 2 options for running everything locally: 

1. Building docker images & using docker-compose **OR**
2. Executing `poetry run...` commands. 

Please follow the respective option below.

In both cases, shortcut `make` commands have been provided.  These should be run from the repository root. 
If you are unable to run the commands, then look at the [Makefile](../Makefile) for the corresponding command. 

<br>

## Option 1: using Docker 

### Build 

Build the individual docker images: 

```bash 
make backend-build    # for the backend (restaurant) APIs 
make chat-build       # for Chat API to interact with the agent/LLM
make ui-build         # for serving front-end Chat UI
```

### Run

The individual containers can be run with `make backend-run` and `make chat-run`. However, you should 
run them using docker-compose for a bridge network to enable communication between the containers:

```bash 
docker-compose up 
```

This will also use propagate the environment variables within the root `.env` file.

You should now be able to view: 
- http://localhost:8000/docs - Backend API 
- http://localhost:3000/docs - Chat API 


<br>

## Option 2: using poetry & local virtualenv

### Running the backend (restaurant) APIs: 

To start FastAPI (located within `/restaurant-api/src`) using the virtualenv created by Poetry: 

```bash 
make backend-serve
```

You should now be able to view the Swagger UI at http://localhost:8000/docs.  

### Running the Chat API: 

To start FastAPI (located within `/chat-api`) using the virtualenv created by Poetry: 

```bash 
make chat-serve
```

You should now be able to view the Swagger UI at http://localhost:3000/docs . 

<br>


## Testing 

Regardless of the method used, you should have the APIs running now. 

Try using http://localhost:8000/docs to explore the data in the backend Restaurant database. 

Then try sending a request to the agent using the Swagger UI at http://localhost:3000/docs 

## Using notebooks 

You can use Jupyter Lab to run notebooks: 

```bash 
make jupyter       # alias for `poetry run jupyter lab` 
```

A browser window should open at http://localhost:8888 where you can navigate to open notebooks. 

<br>

## Running the chat UI frontend 

A React frontend is also available.  Assuming that you have Node installed, you can install dependencies & run the frontend using:

```bash
make ui-install 
make ui-serve 
```

You should then be able to access a UI on http://localhost:8080.  By default, this will send requests to the Chat API at http://localhost:3000/chat 
