import pytest
from sqlalchemy.orm import Session

from src.app.db.models import Customer, MenuItem, Order, OrderItem


# Example of using pytest.mark.parametrize to include descriptions
@pytest.mark.parametrize("description, menu_item_data", [
    ("Creating a vegetarian pizza", {
        "name": "Margherita",
        "price": 9.99,
        "ingredients": "tomato sauce, mozzarella cheese, fresh basil",
        "category": "Pizza",
        "labels": "Vegetarian",
        "available_monday": True
    }),
    ("Creating a pepperoni pizza", {
        "name": "Pepperoni",
        "price": 11.99,
        "ingredients": "tomato sauce, mozzarella cheese, pepperoni",
        "category": "Pizza",
        "labels": "",
        "available_monday": False
    }),
])
def test_create_menu_item(db_session: Session, description, menu_item_data):
    print(f"\n{description}")  # Print the description at the beginning of the test
    menu_item = MenuItem(**menu_item_data)
    db_session.add(menu_item)
    db_session.commit()

    # Query the menu item
    added_item = db_session.query(MenuItem).filter_by(name=menu_item_data["name"]).first()
    assert added_item is not None
    assert added_item.price == menu_item_data["price"]
    assert added_item.available_monday == menu_item_data["available_monday"]


# Test creating and querying Customer
def test_create_customer(db_session: Session):
    customer = Customer(
        firstname="Bart",
        lastname="Simpson",
        email="bart@simpson.com",
        external_id="#1234",
        card_digits="8743",
        street="1234 Elm St",
        city="Springfield",
        state="IL",
        zip="62701",
        country="USA",
        special=True,
        phone="555-555-5555"
    )
    db_session.add(customer)
    db_session.commit()

    # Query the customer
    added_customer = db_session.query(Customer).filter_by(email="bart@simpson.com").first()
    assert added_customer is not None
    assert added_customer.firstname == "Bart"
    assert added_customer.special is True


# Test creating and querying Order
def test_create_order(db_session: Session):
    # First, create a customer
    customer = Customer(
        firstname="Homer",
        lastname="Simpson",
        email="homer@simpson.com",
        external_id="#5678",
        card_digits="6295",
        street="742 Evergreen Terrace",
        city="Springfield",
        state="IL",
        zip="62701",
        country="USA",
        special=True,
        phone="555-555-5556"
    )
    db_session.add(customer)
    db_session.commit()

    # Then, create an order for the customer
    order = Order(
        customer_id=customer.id,
        total_amount=50.00
    )
    db_session.add(order)
    db_session.commit()

    # Query the order
    added_order = db_session.query(Order).filter_by(customer_id=customer.id).first()
    assert added_order is not None
    assert added_order.total_amount == 50.00


# Test creating and querying OrderItem
def test_create_order_item(db_session: Session):
    # Create related entities
    customer = Customer(
        firstname="Margie",
        lastname="Simpson",
        email="margie@simpson.com",
        external_id="#9101",
        card_digits="4801",
        street="742 Evergreen Terrace",
        city="Springfield",
        state="IL",
        zip="62701",
        country="USA"
    )
    menu_item = MenuItem(
        name="Pepperoni",
        price=11.99,
        ingredients="tomato sauce, mozzarella cheese, pepperoni",
        category="Pizza",
    )
    db_session.add(customer)
    db_session.add(menu_item)
    db_session.commit()

    # Create an order
    order = Order(
        customer_id=customer.id,
        total_amount=11.99
    )
    db_session.add(order)
    db_session.commit()

    # Create an order item
    order_item = OrderItem(
        order_id=order.id,
        menu_item_id=menu_item.id,
        quantity=1,
        note="Extra pepperoni"
    )
    db_session.add(order_item)
    db_session.commit()

    # Query the order item
    added_order_item = db_session.query(OrderItem).filter_by(order_id=order.id).first()
    assert added_order_item is not None
    assert added_order_item.quantity == 1
    assert added_order_item.note == "Extra pepperoni"
