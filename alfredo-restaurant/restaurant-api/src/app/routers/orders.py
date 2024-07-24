from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..db.database import get_db
from ..db.models import Customer, MenuItem, Order, OrderItem, OrderStatus
from .schemas import OrderCreate, OrderInDB, OrderItemCreate, OrderItemInDB, OrderUpdate

router = APIRouter()


@router.get("/orders", response_model=List[OrderInDB])
def get_orders(db: Session = Depends(get_db)):
    return db.query(Order).all()


@router.get("/orders/{order_id}", response_model=OrderInDB)
def get_order_by_id(order_id: int, db: Session = Depends(get_db)):
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order


@router.get("/orders_by_user/{user_id}", response_model=List[OrderInDB])
def get_orders_by_user_id(user_id: int, db: Session = Depends(get_db)):
    """Retrieve orders for a specific user by customer ID."""
    orders = db.query(Order).filter(Order.customer_id == user_id).all()
    if not orders:
        raise HTTPException(status_code=404, detail="No orders found for this user")
    return orders


@router.post("/orders", response_model=OrderInDB)
def create_order(order_create: OrderCreate, db: Session = Depends(get_db)):
    db_customer = db.query(Customer).filter(Customer.id == order_create.customer_id).first()
    if not db_customer:
        raise HTTPException(status_code=404, detail="Customer not found")

    order_items = []
    total_amount = 0
    for item in order_create.items:
        db_menu_item = db.query(MenuItem).filter(MenuItem.id == item.menu_item_id).first()
        if not db_menu_item:
            raise HTTPException(status_code=404, detail=f"Menu item with id {item.menu_item_id} not found")

        order_item = OrderItem(
            menu_item_id=item.menu_item_id,
            quantity=item.quantity,
            note=item.note,
            menu_item=db_menu_item
        )
        order_items.append(order_item)
        total_amount += db_menu_item.price * item.quantity

    db_order = Order(
        customer_id=order_create.customer_id,
        total_amount=total_amount,
        items=order_items,
        status=OrderStatus.PENDING  # default status
    )

    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order


@router.patch("/orders/{order_id}", response_model=OrderInDB)
def update_order(order_id: int, order_update: OrderUpdate, db: Session = Depends(get_db)):
    db_order = db.query(Order).filter(Order.id == order_id).first()
    if not db_order:
        raise HTTPException(status_code=404, detail="Order not found")

    update_data = order_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_order, key, value)

    db.commit()
    db.refresh(db_order)
    return db_order
