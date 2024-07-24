from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from ..db.database import get_db
from ..db.models import Customer
from .schemas import CustomerCreate, CustomerInDB, CustomerUpdate

router = APIRouter()


@router.get("/customers", response_model=List[CustomerInDB])
def get_customers(
        db: Session = Depends(get_db),
        firstname: Optional[str] = Query(None),
        lastname: Optional[str] = Query(None),
        email: Optional[str] = Query(None),
        external_id: Optional[str] = Query(None),
        phone: Optional[str] = Query(None)
):
    query = db.query(Customer)
    if firstname:
        query = query.filter(Customer.firstname.ilike(f"%{firstname}%"))
    if lastname:
        query = query.filter(Customer.lastname.ilike(f"%{lastname}%"))
    if email:
        query = query.filter(Customer.email.ilike(f"%{email}%"))
    if external_id:
        query = query.filter(Customer.external_id == external_id)
    if phone:
        query = query.filter(Customer.phone.ilike(f"%{phone}%"))
    return query.all()


@router.get("/customers/{customer_id}", response_model=CustomerInDB)
def get_customer_by_id(customer_id: int, db: Session = Depends(get_db)):
    customer = db.query(Customer).filter(Customer.id == customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer


@router.post("/customers", response_model=CustomerInDB)
def create_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
    db_customer = Customer(
        firstname=customer.firstname,
        lastname=customer.lastname,
        email=customer.email,
        phone=customer.phone,
        special=customer.special,
        card_digits=customer.card_digits,
        external_id=customer.external_id,
        street=customer.street,
        city=customer.city,
        state=customer.state,
        zip=customer.zip,
        country=customer.country,
    )
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer


@router.patch("/customers/{customer_id}", response_model=CustomerInDB)
def update_customer(customer_id: int, customer_update: CustomerUpdate, db: Session = Depends(get_db)):
    db_customer = db.query(Customer).filter(Customer.id == customer_id).first()
    if not db_customer:
        raise HTTPException(status_code=404, detail="Customer not found")

    update_data = customer_update.dict(exclude_unset=True) # Exclude fields not provided in the request
    for key, value in update_data.items():
        setattr(db_customer, key, value)

    db.commit()
    db.refresh(db_customer)
    return db_customer