from typing import Optional

import requests
from langchain.tools import tool
from langchain.pydantic_v1 import BaseModel, Field

from .config import restaurant_api_base

class OpeningHoursToolInputSchema(BaseModel):
    day: Optional[str] = Field(description="The day of the week for which you want the opening hours. eg. 'Monday'")
    special: Optional[bool] = Field(description="Whether the user is a special member.")


@tool("OpeningHoursTool", args_schema=OpeningHoursToolInputSchema)
def opening_hours_tool(day=None, special=False):
    """
    Fetches opening hours from the API, optionally filtered by day and special status.

    Args:
        - day (str, optional): Day of the week to filter the opening hours.
        - special (bool, optional): Whether to fetch special (VIP) opening hours.

    Returns:
        - A list of opening hours or an error message.
    """
    # Construct the URL and query parameters
    url = f"{restaurant_api_base}/api/opening-hours"
    params = {}
    if day:
        params['day'] = day
    if special:
        params['special'] = '1'

    # Make the GET request
    response = requests.get(url, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        return response.json()  # Return the list of opening hours as JSON
    else:
        return f"Error {response.status_code}: {response.text}"  # Return error message if not successful

