import pytest
from pydantic import ValidationError

from src.app.routers.schemas import MenuItemCreate, MenuItemInDB, MenuItemUpdate


# Test MenuItem schemas
def test_menu_item_create():
    item = MenuItemCreate(
        name="Spaghetti Carbonara",
        price=12.99,
        ingredients="spaghetti, bacon, eggs, parmesan cheese",
        category="Pasta",
        labels="",
        available_monday=True
    )
    assert item.name == "Spaghetti Carbonara"
    assert item.price == 12.99
    assert item.available_monday is True
    assert item.available_tuesday is False  # default value

def test_menu_item_update():
    item_update = MenuItemUpdate(
        price=13.99,
        available_monday=False
    )
    assert item_update.price == 13.99
    assert item_update.available_monday is False

def test_menu_item_in_db():
    item_in_db = MenuItemInDB(
        id=1,
        name="Spaghetti Bolognese",
        price=11.99,
        ingredients="spaghetti, ground beef, tomato sauce, onions, garlic, carrots, celery",
        category="Pasta",
        labels="",
        available_monday=True,
        available_tuesday=False,
        available_wednesday=True,
        available_thursday=False,
        available_friday=False,
        available_saturday=False,
        available_sunday=True
    )
    assert item_in_db.id == 1
    assert item_in_db.name == "Spaghetti Bolognese"
    assert item_in_db.available_wednesday is True


# Validation tests for schema errors
def test_invalid_menu_item():
    with pytest.raises(ValidationError):
        MenuItemCreate(
            name="",
            price="free",  # invalid price type
            ingredients="spaghetti",
            category="Pasta"
        )
