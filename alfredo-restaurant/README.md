#  Restaurant project

Welcome to **Alfredo restaurant** app.

Here, you will find several directories: 

```bash 
├── chat-api                # Chat API used by the Guardrails lab 
├── chat-ui                 # Chat front-end for sending requests to & seeing results from the Chat API
├── restaurant-api          # Chat front-end for sending requests to & seeing results from the Chat API
└── infra                   # Info to deploy Azure resources for the lab 
└── docs                    # Info on deployment 
```

## Azure resources required

You will require an Azure OpenAI model deployed - at least GPT-4 (and preferably a recent version of GPT4-Turbo)
with a high rate limit (preferably 40,000 TPM (tokens per minute)  if possible).

You can create one via the Azure admin portal:

- [Manual deployment via Azure portal](infra/manual-deployment-in-azure-portal.md)

You will need the following for your deployed model:

- Endpoint name
- Deployment name
- API key
- API version

(Please see the guidance above on where to find these.)

## Environment setup

You have 2 options for environment setup, installation of APIs and using Notebooks. Please choose the one which suits you best.

1. [**Devcontainer & Docker-compose**](docs/environment-setup-devcontainer.md) 

2. [**Poetry & python**](docs/environment-setup-local-virtualenv) - for developers comfortable with the command line, pyenv and poetry.

We recommend the devcontainer route.

## Next step

After setting up the project, see the [Guardrail Lab](../guardrail-lab/00-Start-Here/README.md) to get started with Guardrails.
