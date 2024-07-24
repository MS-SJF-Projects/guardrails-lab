from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from ..db.database import get_db
from ..db.models import MenuItem
from .schemas import MenuItemCreate, MenuItemInDB, MenuItemUpdate

router = APIRouter()


@router.get("/menu-items", response_model=List[MenuItemInDB], tags=["Menu Items"])
def get_menu_items(
        db: Session = Depends(get_db),
        name: Optional[str] = Query(None),
        category: Optional[str] = Query(None),
        labels: Optional[str] = Query(None),
        ingredients: Optional[str] = Query(None)
):
    query = db.query(MenuItem)
    if name:
        query = query.filter(MenuItem.name.ilike(f"%{name}%"))
    if category:
        query = query.filter(MenuItem.category.ilike(f"%{category}%"))
    if labels:
        query = query.filter(MenuItem.labels.ilike(f"%{labels}%"))
    if ingredients:
        query = query.filter(MenuItem.ingredients.ilike(f"%{ingredients}%"))
    return query.all()


@router.get("/menu-items/{item_id}", response_model=MenuItemInDB, tags=["Menu Items"])
def get_menu_item_by_id(item_id: int, db: Session = Depends(get_db)):
    menu_item = db.query(MenuItem).filter(MenuItem.id == item_id).first()
    if not menu_item:
        raise HTTPException(status_code=404, detail="Menu item not found")
    return menu_item


@router.get("/menu/{day}", response_model=List[MenuItemInDB], tags=["Menu by Day"])
def get_menu_by_day(day: str, db: Session = Depends(get_db)):
    day_map = {
        "monday": MenuItem.available_monday,
        "tuesday": MenuItem.available_tuesday,
        "wednesday": MenuItem.available_wednesday,
        "thursday": MenuItem.available_thursday,
        "friday": MenuItem.available_friday,
        "saturday": MenuItem.available_saturday,
        "sunday": MenuItem.available_sunday
    }
    if day.lower() not in day_map:
        raise HTTPException(status_code=400, detail="Invalid day")

    return db.query(MenuItem).filter(day_map[day.lower()] == True).all()


@router.post("/menu-items", response_model=MenuItemInDB, tags=["Menu Items"])
def create_menu_item(menu_item: MenuItemCreate, db: Session = Depends(get_db)):
    db_menu_item = MenuItem(**menu_item.dict())
    db.add(db_menu_item)
    db.commit()
    db.refresh(db_menu_item)
    return db_menu_item


@router.patch("/menu-items/{item_id}", response_model=MenuItemInDB, tags=["Menu Items"])
def update_menu_item(item_id: int, menu_item_update: MenuItemUpdate, db: Session = Depends(get_db)):
    db_menu_item = db.query(MenuItem).filter(MenuItem.id == item_id).first()
    if not db_menu_item:
        raise HTTPException(status_code=404, detail="Menu item not found")

    update_data = menu_item_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_menu_item, key, value)

    db.commit()
    db.refresh(db_menu_item)
    return db_menu_item

