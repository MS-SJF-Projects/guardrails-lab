from typing import List, Dict, Any, Optional

import requests

from langchain.pydantic_v1 import BaseModel, Field
from langchain.tools import tool

from .config import restaurant_api_base

class CustomerRetrievalToolInputSchema(BaseModel):
    email: Optional[str] = Field(description="The email address of the customer")
    phone: Optional[str] = Field(description="The phone numbers of the customer")
    firstname: Optional[str] = Field(description="The first name of the customer")
    lastname: Optional[str] = Field(description="The last name of the customer")


@tool("CustomerRetrievalTool", args_schema=CustomerRetrievalToolInputSchema)
def customer_retrieval_tool(lastname: str = None,
                  firstname: str = None,
                  email: str = None,
                  phone: str = None) -> Dict[str, Any]:
    """
    Get a customer by their first, last name, email, phone or combination of such.

    To use the tool directly, call the `.invoke()` method provided by the @tool
    decorator with a dictionary of the provided arguments:

        customer_retrieval_tool.invoke({'lastname': 'Simpson'})

    Args:
        firstname (str): The first name of the customer.
        lastname (str): The last name of the customer.
        email (str): The email address of the customer.
        phone (str): The phone number of the customer.

    Returns:
        List[Dict[str, Any]]: The customer data.
    """
    url = f"{restaurant_api_base}/api/customers"
    params = {'firstname': firstname, 'lastname': lastname, 'email': email, 'phone': phone}
    response = requests.get(url, params=params)
    response.raise_for_status()     # Raise an error for bad status codes
    return response.json()


