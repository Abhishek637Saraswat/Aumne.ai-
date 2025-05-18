from pydantic import BaseModel, Field, constr
from datetime import datetime
from typing import Optional

class FlightCreate(BaseModel):
    flight_number: str
    airline: str
    departure: str
    destination: str
    departure_time: datetime
    total_seats: int = Field(gt=0)

class FlightOut(FlightCreate):
    id: int
    available_seats: int

    model_config = {
        "from_attributes": True
    }

class BookingCreate(BaseModel):
    passenger_name: str
    passport_number: constr(pattern=r"^[A-Z][0-9]{7}$")   # Format: 1 capital letter + 7 digits

class BookingOut(BaseModel):
    id: int
    passenger_name: str
    passport_number: str
    flight_id: int
    is_cancelled: bool



    model_config = {
        "from_attributes": True
    }
