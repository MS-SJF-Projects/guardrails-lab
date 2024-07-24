from datetime import datetime
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, ConfigDict, EmailStr


class MenuItemBase(BaseModel):
    name: str
    price: float
    ingredients: str
    category: str
    labels: Optional[str] = None
    available_monday: bool = False
    available_tuesday: bool = False
    available_wednesday: bool = False
    available_thursday: bool = False
    available_friday: bool = False
    available_saturday: bool = False
    available_sunday: bool = False

    model_config = ConfigDict(from_attributes=True)


class MenuItemCreate(MenuItemBase):
    pass

class MenuItemUpdate(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    ingredients: Optional[str] = None
    category: Optional[str] = None
    labels: Optional[str] = None
    available_monday: Optional[bool] = None
    available_tuesday: Optional[bool] = None
    available_wednesday: Optional[bool] = None
    available_thursday: Optional[bool] = None
    available_friday: Optional[bool] = None
    available_saturday: Optional[bool] = None
    available_sunday: Optional[bool] = None

    model_config = ConfigDict(from_attributes=True)


class MenuItemInDB(MenuItemBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class CustomerBase(BaseModel):
    firstname: str
    lastname: str
    email: EmailStr
    phone: Optional[str] = None
    special: Optional[bool] = False
    card_digits: str
    external_id: str
    street: str
    city: str
    state: str
    zip: str
    country: str


class CustomerCreate(CustomerBase):
    pass


# Defaults are required to be None
# https://docs.pydantic.dev/latest/migration/#required-optional-and-nullable-fields
class CustomerUpdate(BaseModel):
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    special: Optional[bool] = None
    card_digits: Optional[str] = None
    street: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    zip: Optional[str] = None
    country: Optional[str] = None


class CustomerInDB(CustomerBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class OrderStatus(str, Enum):
    pending = "pending"
    in_progress = "in_progress"
    delivered = "delivered"
    cancelled = "cancelled"


class OrderItemBase(BaseModel):
    menu_item_id: int
    quantity: int
    note: Optional[str] = None


class OrderItemCreate(OrderItemBase):
    pass


class OrderItemInDB(OrderItemBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class OrderBase(BaseModel):
    customer_id: int
    order_date: Optional[datetime] = None
    status: OrderStatus = OrderStatus.pending
    total_amount: Optional[float] = None


class OrderCreate(OrderBase):
    items: List[OrderItemCreate]


class OrderUpdate(BaseModel):
    status: Optional[OrderStatus]


class OrderInDB(OrderBase):
    id: int
    items: List[OrderItemInDB]

    model_config = ConfigDict(from_attributes=True)


class OpeningHoursSchema(BaseModel):
    id: int
    day: str
    start: Optional[str] = None
    end: Optional[str] = None
    status: str
    is_special: bool

    model_config = ConfigDict(from_attributes=True)

