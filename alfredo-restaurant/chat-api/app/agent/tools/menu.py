from typing import List, Dict, Any

import requests
from langchain.pydantic_v1 import BaseModel, Field
from langchain.tools import tool


from .config import restaurant_api_base

class DailyMenuInputSchema(BaseModel):
    """Defines the input schema for the daily menu tool."""
    day: str = Field(description="The day of the week for which you wish to know the menu. e.g. 'Monday'")


@tool("DailyMenuTool", args_schema=DailyMenuInputSchema)
def daily_menu_tool(day: str) -> List[Dict[str, Any]]:
    """
    Get the full menu available on a particular day of the week.

    Args:
        day (str): The day of the week (e.g., "Monday").

    Returns:
        List[Dict[str, Any]]: A list of menu items.
    """
    print(f"Checking the menu for {day}")
    url = f"{restaurant_api_base}/api/menu-items"
    params = {'day': day}
    response = requests.get(url, params=params)
    response.raise_for_status()  # Raise an error for bad status codes
    return response.json()
