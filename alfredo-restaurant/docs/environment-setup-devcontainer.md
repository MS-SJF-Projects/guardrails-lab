# Using VS Code devcontainers 


The repository includes a [Dev container](https://code.visualstudio.com/docs/devcontainers/containers) to make provisioning the environment and required dependencies very easy.  
You will need: 

- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- [VSCode](https://code.visualstudio.com/) 
- [Dev Container Extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) installed.


## Configure environment variables 

Create a .env file in the root directory of the repository with these details:

```bash 
AZURE_OPENAI_ENDPOINT=https://<your-endpoint>.openai.azure.com/
AZURE_OPENAI_DEPLOYMENT=gpt-4-32k        # or whatever you named your deployment
AZURE_OPENAI_API_KEY=***********
AZURE_OPENAI_API_VERSION=2024-02-01

TIMEZONE=Europe/Berlin
VITE_CHAT_API=http://127.0.0.1:3000
```


## Open code in Devcontainer  

Clone the repository & open it with VS Code. 

Press `Ctrl` + `Shift` + `P` in VS code:
```
> Dev Containers: Rebuild and Reopen in Container
```

Wait for the dev container to be created.


## Run APIs using docker-compose 

Build the docker images: 

```bash
make backend-build  # for the backend (restaurant) APIs 
make chat-build     # for Chat API to interact with the agent/LLM
make ui-build       # for serving front-end Chat UI 
```

Run everything with `docker-compose`:

```bash
docker-compose up
```


## Test 

That's it.  You should be able to connect ot the following: 

- http://localhost:8000/docs - Swagger UI for the backend (retaurant) API
- http://localhost:3000/docs - Swagger UI for the Chat agent API 
- http://localhost:8080 - Chat UI front-end 

