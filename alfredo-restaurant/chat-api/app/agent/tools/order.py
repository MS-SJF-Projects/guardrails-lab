import requests

from typing import List, Dict, Any, Optional

from langchain.pydantic_v1 import BaseModel, Field
from langchain.tools import tool


from .config import restaurant_api_base

class RetrieveOrderInputSchema(BaseModel):
    order_id: int = Field(description="The order ID for which you wish to retrieve the order.")


class CancelOrderInputSchema(BaseModel):
    order_id: int = Field(description="The order ID for order you wish to cancel.")


class RetrieveUserOrdersInputSchema(BaseModel):
    user_id: int = Field(description="The user ID for which you wish to retrieve orders.")


@tool("RetrieveOrderTool", args_schema=RetrieveOrderInputSchema)
def retrieve_order_tool(order_id: int) -> Dict[str, Any]:
    """
    Retrieve an order by its ID.

    Args:
        order_id (int): The ID of the order.

    Returns:
        Dict[str, Any]: The order status and details.
    """
    url = f"{restaurant_api_base}/api/orders/{order_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "unable to retrieve order"}


@tool("RetrieveUserOrdersTool", args_schema=RetrieveUserOrdersInputSchema)
def retrieve_user_orders_tool(user_id: int):
    """
    Retrieve orders for a specific user.

    Args:
        user_id (int): The ID of the customer.

    Returns:
        Dict[str, Any]: The order status and details.
    """
    url = f"{restaurant_api_base}/api/orders_by_user/{user_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "unable to retrieve orders"}


@tool("CancelOrderTool", args_schema=CancelOrderInputSchema)
def cancel_order_tool(order_id):
    """
    Cancels an order by setting its status to 'cancelled'.

    Args:
    - api_url (str): The base URL of the API.
    - order_id (int): The ID of the order to cancel.

    Returns:
    - The updated order information or an error message.
    """
    url = f"{restaurant_api_base}/api/orders/{order_id}"
    data = {'status': 'cancelled'}
    response = requests.patch(url, json=data)
    if response.status_code == 200:
        return response.json()  # Return the updated order information
    else:
        return f"Error {response.status_code}: {response.text}"


# def create_order(customer_id: int, items: List[Dict[str, Any]]) -> Dict[str, Any]:
#     """
#     Create a new order for a customer.
#
#     Args:
#         customer_id (int): The ID of the customer.
#         items (List[Dict[str, Any]]): A list of items with menu_item_id and quantity.
#
#     Returns:
#         Dict[str, Any]: The created order details.
#     """
#     url = f"http://localhost:8000/api/orders"
#     payload = {
#         'customer_id': customer_id,
#         'items': items
#     }
#     headers = {'Content-Type': 'application/json'}
#     response = requests.post(url, data=json.dumps(payload), headers=headers)
#     response.raise_for_status()  # Raise an error for bad status codes
#     return response.json()
#