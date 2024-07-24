import json
from pathlib import Path
from unittest.mock import mock_open, patch

import pytest
from sqlalchemy.orm import Session

from src.app.db.initial_data_loader import load_customers, load_regular_menus
from src.app.db.models import Customer, MenuItem

# Mock data similar to what you'd have in your JSON files
mock_menu_data = {
    "pasta": [
        {
            "name": "Spaghetti Carbonara",
            "price": 12.99,
            "ingredients": ["spaghetti", "bacon", "eggs", "parmesan cheese"],
            "label": ""
        }
        # Add more items as needed for the test
    ]
}

# Use different customers to avoid conflict (UNIQUE constraint) with those in the test_db_models.py
mock_customers_data = [
    {
        "firstname": "Dastardly",
        "lastname": "Dick",
        "email": "dick@dastardly.com",
        "id": "#1212",
        "card_digits": "1212",
        "address": {
            "street": "123 Perilous Path",
            "city": "Villainsville",
            "state": "NY",
            "zip": "10001",
            "country": "USA"
        },
        "special": "true",
        "phone": "555-555-5580"
    },
    {
        "firstname": "Muttley",
        "lastname": "Dog",
        "email": "muttley@dog.com",
        "id": "#2323",
        "card_digits": "2323",
        "address": {
            "street": "123 Perilous Path",
            "city": "Villainsville",
            "state": "NY",
            "zip": "10001",
            "country": "USA"
        },
        "special": "false",
        "phone": "555-555-5581"
    }
]

@pytest.fixture
def mock_menu_json():
    """Mock menu.json data."""
    mock_data = json.dumps(mock_menu_data)
    with patch("builtins.open", mock_open(read_data=mock_data)):
        yield

@pytest.fixture
def mock_customers_json():
    """Mock customers.json data."""
    mock_data = json.dumps(mock_customers_data)
    with patch("builtins.open", mock_open(read_data=mock_data)):
        yield

def test_load_regular_menus(db_session: Session, mock_menu_json):
    load_regular_menus(db_session)

    # Verify that the data was loaded correctly
    menu_items = db_session.query(MenuItem).all()
    assert len(menu_items) == len(mock_menu_data["pasta"])  # Adjust based on the mock data
    assert menu_items[0].name == "Spaghetti Carbonara"
    assert menu_items[0].price == 12.99

def test_load_customers(db_session: Session, mock_customers_json):
    load_customers(db_session)

    # Verify that the data was loaded correctly
    customers = db_session.query(Customer).all()
    assert len(customers) == len(mock_customers_data)  # Adjust based on the mock data
    assert customers[0].firstname == "Dastardly"
    assert customers[0].email == "dick@dastardly.com"
