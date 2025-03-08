from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Booking, Show
from database import get_db
from auth import get_current_user

router = APIRouter()

@router.post("/bookings/")
def book_ticket(show_id: int, booked_seats: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    show = db.query(Show).filter(Show.id == show_id).first()
    if not show or show.available_seats < booked_seats:
        raise HTTPException(status_code=400, detail="Not enough seats available")
    
    # Dynamic Pricing
    demand_factor = 1.0 + ((show.total_seats - show.available_seats) / show.total_seats) * 0.5
    final_price = int(show.base_price * demand_factor)

    show.available_seats -= booked_seats
    booking = Booking(user_id=user.id, show_id=show_id, booked_seats=booked_seats)
    db.add(booking)
    db.commit()

    return {"message": "Tickets booked successfully!", "price_per_ticket": final_price}
