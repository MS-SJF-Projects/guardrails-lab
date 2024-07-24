from datetime import datetime

from src.app.routers.schemas import OrderCreate, OrderInDB, OrderItemCreate, OrderItemInDB, OrderStatus, OrderUpdate


# Test OrderItem schemas
def test_order_item_create():
    order_item = OrderItemCreate(
        menu_item_id=1,
        quantity=2,
        note="Extra cheese"
    )
    assert order_item.menu_item_id == 1
    assert order_item.quantity == 2
    assert order_item.note == "Extra cheese"

def test_order_item_in_db():
    order_item_in_db = OrderItemInDB(
        id=1,
        menu_item_id=2,
        quantity=1,
        note="No onions"
    )
    assert order_item_in_db.id == 1
    assert order_item_in_db.note == "No onions"

# Test Order schemas
def test_order_create():
    order = OrderCreate(
        customer_id=1,
        order_date=datetime(2023, 6, 15, 12, 0),
        status=OrderStatus.pending,
        total_amount=25.98,
        items=[OrderItemCreate(menu_item_id=1, quantity=2, note="Extra cheese")]
    )
    assert order.customer_id == 1
    assert len(order.items) == 1
    assert order.items[0].note == "Extra cheese"

def test_order_update():
    order_update = OrderUpdate(
        status=OrderStatus.delivered
    )
    assert order_update.status == OrderStatus.delivered

def test_order_in_db():
    order_in_db = OrderInDB(
        id=1,
        customer_id=2,
        order_date=datetime(2023, 6, 15, 12, 0),
        status=OrderStatus.in_progress,
        total_amount=50.99,
        items=[OrderItemInDB(id=1, menu_item_id=2, quantity=1, note="No onions")]
    )
    assert order_in_db.id == 1
    assert order_in_db.status == OrderStatus.in_progress
    assert len(order_in_db.items) == 1
