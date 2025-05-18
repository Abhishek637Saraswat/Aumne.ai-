from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, crud
from app.database import SessionLocal

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/bookings/", response_model=list[schemas.BookingOut])
def get_all_bookings(db: Session = Depends(get_db)):
    return crud.get_all_bookings(db)


@router.post("/flights/", response_model=schemas.FlightOut)
def create_flight(flight: schemas.FlightCreate, db: Session = Depends(get_db)):
    return crud.create_flight(db, flight)

@router.get("/flights/", response_model=list[schemas.FlightOut])
def get_flights(db: Session = Depends(get_db)):
    return crud.get_flights(db)

@router.get("/flights/{flight_id}", response_model=schemas.FlightOut)
def get_flight(flight_id: int, db: Session = Depends(get_db)):
    db_flight = crud.get_flight(db, flight_id)
    if not db_flight:
        raise HTTPException(status_code=404, detail="Flight not found")
    return db_flight

@router.post("/flights/{flight_id}/book", response_model=schemas.BookingOut)
def book_flight(flight_id: int, booking: schemas.BookingCreate, db: Session = Depends(get_db)):
    return crud.book_ticket(db, flight_id, booking)

@router.delete("/bookings/{booking_id}")
def cancel_booking(booking_id: int, db: Session = Depends(get_db)):
    return crud.cancel_booking(db, booking_id)
