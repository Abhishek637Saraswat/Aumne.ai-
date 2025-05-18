from sqlalchemy.orm import Session
from fastapi import HTTPException
from . import models, schemas
from datetime import datetime
import re


# def get_all_bookings(db: Session):
#     bookings = db.query(models.Booking).all()
#     enriched = []
#
#     for booking in bookings:
#         flight = db.query(models.Flight).filter_by(id=booking.flight_id).first()
#         status = "Unknown"
#
#         if booking.is_cancelled:
#             status = "Cancelled"
#         elif flight and flight.departure_time < datetime.now():
#             status = "Completed"
#         elif flight:
#             time_left = flight.departure_time - datetime.now()
#             minutes = int(time_left.total_seconds() // 60)
#             hours, minutes = divmod(minutes, 60)
#             status = f"Departing in {hours}h {minutes}m"
#
#         enriched.append({
#             "id": booking.id,
#             "passenger_name": booking.passenger_name,
#             "flight_id": booking.flight_id,
#             "is_cancelled": booking.is_cancelled,
#             "status": status
#         })
#
#     return enriched

def create_flight(db: Session, flight: schemas.FlightCreate):
    db_flight = models.Flight(
        flight_number=flight.flight_number,
        airline=flight.airline,
        departure=flight.departure,
        destination=flight.destination,
        departure_time=flight.departure_time,
        total_seats=flight.total_seats,
        available_seats=flight.total_seats,
    )
    db.add(db_flight)
    db.commit()
    db.refresh(db_flight)
    return db_flight


def get_flights(db: Session):
    return db.query(models.Flight).all()

def get_all_bookings(db: Session):
    return db.query(models.Booking).all()


def get_flight(db: Session, flight_id: int):
    return db.query(models.Flight).filter(models.Flight.id == flight_id).first()

def book_ticket(db: Session, flight_id: int, booking: schemas.BookingCreate):
    # Validate passport format again (redundant, but defensive)
    if not re.match(r"^[A-Z][0-9]{7}$", booking.passport_number):
        raise HTTPException(status_code=422, detail="Invalid passport number format. Expected: A1234567")

    # Check if flight exists
    flight = get_flight(db, flight_id)
    if not flight:
        raise HTTPException(status_code=404, detail="Flight not found")

    # Check for available seats
    if flight.available_seats <= 0:
        raise HTTPException(status_code=400, detail="No available seats")

    # Check for duplicate active booking with the same passport number
    existing_booking = db.query(models.Booking).filter(
        models.Booking.passport_number == booking.passport_number,
        models.Booking.is_cancelled == False
    ).first()

    if existing_booking:
        raise HTTPException(status_code=400, detail=f"An active booking already exists for passport number {booking.passport_number}")

    # Create new booking
    db_booking = models.Booking(
        passenger_name=booking.passenger_name,
        passport_number=booking.passport_number,
        flight_id=flight_id
    )
    flight.available_seats -= 1
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking
# def book_ticket(db: Session, flight_id: int, booking: schemas.BookingCreate):
#     flight = get_flight(db, flight_id)
#     if not flight:
#         raise HTTPException(status_code=404, detail="Flight not found")
#     if flight.available_seats <= 0:
#         raise HTTPException(status_code=400, detail="No available seats")
#     if db.query(models.Booking).filter(models.Booking.passport_number == booking.passport_number,
#                                        models.Booking.is_cancelled == False).first():
#         raise HTTPException(status_code=400, detail="Passport number already used")
#
#     db_booking = models.Booking(
#         passenger_name=booking.passenger_name,
#         passport_number=booking.passport_number,
#         flight_id=flight_id
#     )
#     flight.available_seats -= 1
#     db.add(db_booking)
#     db.commit()
#     db.refresh(db_booking)
#     return db_booking

'''
def cancel_booking(db: Session, booking_id: int):
    booking = db.query(models.Booking).filter(models.Booking.id == booking_id).first()
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    if booking.is_cancelled:
        raise HTTPException(status_code=400, detail="Booking already cancelled")

    booking.is_cancelled = True
    flight = db.query(models.Flight).filter(models.Flight.id == booking.flight_id).first()
    flight.available_seats += 1
    db.commit()
    return {"message": "Booking cancelled successfully"}
'''
def cancel_booking(db: Session, booking_id: int):
    booking = db.query(models.Booking).filter(models.Booking.id == booking_id).first()
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    if booking.is_cancelled:
        raise HTTPException(status_code=400, detail="Booking already cancelled")

    flight = db.query(models.Flight).filter(models.Flight.id == booking.flight_id).first()
    if flight:
        flight.available_seats += 1

    booking.is_cancelled = True
    db.commit()
    return {"message": "Booking cancelled successfully"}

