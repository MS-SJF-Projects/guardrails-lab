from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..db.database import get_db
from ..db.models import OpeningHours
from .schemas import OpeningHoursSchema

router = APIRouter()


@router.get("/opening-hours", response_model=List[OpeningHoursSchema])
def get_opening_hours_by_day(day: Optional[str] = None, special: Optional[bool] = False, db: Session = Depends(get_db)):
    """Get opening hours by day."""
    query = db.query(OpeningHours)
    if day:
        query = query.filter(OpeningHours.day == day.title())
    if special:
        query = query.filter(OpeningHours.is_special == True)
    opening_hours = query.all()
    if not opening_hours:
        raise HTTPException(status_code=404, detail="No opening hours found based on the filter criteria")
    return opening_hours

