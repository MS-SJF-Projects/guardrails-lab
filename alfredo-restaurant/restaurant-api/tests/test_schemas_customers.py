import pytest
from pydantic import ValidationError

from src.app.routers.schemas import CustomerCreate, CustomerInDB, CustomerUpdate, MenuItemCreate


# Test Customer schemas
def test_customer_create():
    customer = CustomerCreate(
        firstname="John",
        lastname="Doe",
        email="john.doe@example.com",
        phone="555-555-5555",
        special=True,
        card_digits="1234",
        external_id="#1234",
        street="123 Elm St",
        city="Springfield",
        state="IL",
        zip="62701",
        country="USA"
    )
    assert customer.firstname == "John"
    assert customer.special is True


def test_customer_update():
    customer_update = CustomerUpdate(
        email="jane.doe@example.com",
        special=False
    )
    assert customer_update.email == "jane.doe@example.com"
    assert customer_update.special is False

def test_customer_in_db():
    customer_in_db = CustomerInDB(
        id=1,
        firstname="Jane",
        lastname="Doe",
        email="jane.doe@example.com",
        phone="555-555-5556",
        special=False,
        card_digits="5678",
        external_id="#5678",
        street="456 Oak St",
        city="Springfield",
        state="IL",
        zip="62701",
        country="USA"
    )
    assert customer_in_db.id == 1
    assert customer_in_db.lastname == "Doe"



# Validation tests for schema errors
def test_invalid_menu_item():
    with pytest.raises(ValidationError):
        MenuItemCreate(
            name="",
            price="free",  # invalid price type
            ingredients="spaghetti",
            category="Pasta"
        )

def test_invalid_customer():
    with pytest.raises(ValidationError):
        CustomerCreate(
            firstname="John",
            lastname="Doe",
            email="invalid-email",  # invalid email format
            phone="555-555-5555",
            special=True,
            card_digits="1234",
            external_id="#1234",
            street="123 Elm St",
            city="Springfield",
            state="IL",
            zip="62701",
            country="USA"
        )
