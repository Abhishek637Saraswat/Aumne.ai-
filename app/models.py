from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.database import Base

class Flight(Base):
    __tablename__ = "flights"
    id = Column(Integer, primary_key=True, index=True)
    flight_number = Column(String, unique=True, index=True)
    airline = Column(String)
    departure = Column(String)
    destination = Column(String)
    departure_time = Column(DateTime)
    total_seats = Column(Integer)
    available_seats = Column(Integer)

    bookings = relationship("Booking", back_populates="flight")

class Booking(Base):
    __tablename__ = "bookings"
    id = Column(Integer, primary_key=True, index=True)
    passenger_name = Column(String)
    passport_number = Column(String, unique=True)
    flight_id = Column(Integer, ForeignKey("flights.id"))
    is_cancelled = Column(Boolean, default=False)

    flight = relationship("Flight", back_populates="bookings")
