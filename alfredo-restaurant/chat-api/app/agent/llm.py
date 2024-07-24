import os

from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI


# Load environment variables from .env file
load_dotenv()

api_key = os.environ['AZURE_OPENAI_API_KEY']
api_version = os.environ['AZURE_OPENAI_API_VERSION']
endpoint = os.environ['AZURE_OPENAI_ENDPOINT']
deployment = os.environ['AZURE_OPENAI_DEPLOYMENT']

def create_llm(temperature: float = 0.2):
    """
    Returns an instance of the AzureChatOpenAI class based on environment variables.
    """
    return AzureChatOpenAI(
        api_key=api_key,
        api_version=api_version,
        azure_endpoint=endpoint,
        azure_deployment=deployment,
        streaming=False,
        temperature=temperature,
    )
