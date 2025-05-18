# import pytest
# from fastapi.testclient import TestClient
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from app.main import app
# from app.database import Base, get_db
# from app import models
#
# # Test DB setup
# SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
# engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
# TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#
# # Override DB dependency
# def override_get_db():
#     try:
#         db = TestingSessionLocal()
#         yield db
#     finally:
#         db.close()
#
# app.dependency_overrides[get_db] = override_get_db
#
# client = TestClient(app)
#
# # Setup and teardown
# @pytest.fixture(autouse=True)
# def setup_and_teardown():
#     Base.metadata.drop_all(bind=engine)
#     Base.metadata.create_all(bind=engine)
#     yield
#     Base.metadata.drop_all(bind=engine)
#
# # 🧪 TESTS
# def test_create_flight():
#     response = client.post("/flights/", json={
#         "flight_number": "AI101",
#         "airline": "Air India",
#         "departure": "Delhi",
#         "destination": "Mumbai",
#         "departure_time": "2025-05-30T10:00:00",
#         "total_seats": 2
#     })
#     assert response.status_code == 200
#     assert response.json()["flight_number"] == "AI101"
#
# def test_book_flight_success():
#     test_create_flight()
#     response = client.post("/flights/1/book", json={
#         "passenger_name": "John",
#         "passport_number": "A1234567"
#     })
#     assert response.status_code == 200
#     assert response.json()["passenger_name"] == "John"
#
# def test_overbooking():
#     test_book_flight_success()
#     client.post("/flights/1/book", json={
#         "passenger_name": "Jane",
#         "passport_number": "B1234567"
#     })
#     response = client.post("/flights/1/book", json={
#         "passenger_name": "Mark",
#         "passport_number": "C1234567"
#     })
#     assert response.status_code == 400
#     assert response.json()["detail"] == "No available seats"
#
# def test_duplicate_passport():
#     test_book_flight_success()
#     response = client.post("/flights/1/book", json={
#         "passenger_name": "John Duplicate",
#         "passport_number": "A1234567"
#     })
#     assert response.status_code == 400
#     assert response.json()["detail"] == "Passport number already used"
#
# def test_invalid_passport_format():
#     test_create_flight()
#     response = client.post("/flights/1/book", json={
#         "passenger_name": "Alice",
#         "passport_number": "123abc"
#     })
#     assert response.status_code == 422  # Pydantic validation error
#
# def test_cancel_booking():
#     test_book_flight_success()
#     response = client.delete("/bookings/1")
#     assert response.status_code == 200
#     assert response.json()["message"] == "Booking cancelled successfully"


# import pytest
# from fastapi.testclient import TestClient
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.pool import StaticPool
# from app.main import app
# from app.database import Base, get_db
#
# # Use SQLite in-memory DB with StaticPool to share the connection across sessions
# SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
#
# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL,
#     connect_args={"check_same_thread": False},
#     poolclass=StaticPool
# )
#
# TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#
# # Override the get_db dependency to use the test DB session
# def override_get_db():
#     db = TestingSessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
#
# app.dependency_overrides[get_db] = override_get_db
#
# client = TestClient(app)
#
# # Setup and teardown for each test: create fresh tables before test and drop after
# @pytest.fixture(autouse=True)
# def setup_and_teardown():
#     Base.metadata.create_all(bind=engine)
#     yield
#     Base.metadata.drop_all(bind=engine)
#
# # Helper function to create a flight
# def create_flight():
#     response = client.post("/flights/", json={
#         "flight_number": "AI101",
#         "airline": "Air India",
#         "departure": "Delhi",
#         "destination": "Mumbai",
#         "departure_time": "2025-05-30T10:00:00",
#         "total_seats": 2
#     })
#     assert response.status_code == 200
#     return response.json()
#
# # 🧪 TESTS
#
# def test_create_flight():
#     flight = create_flight()
#     assert flight["flight_number"] == "AI101"
#
# def test_book_flight_success():
#     flight = create_flight()
#     response = client.post(f"/flights/{flight['id']}/book", json={
#         "passenger_name": "John",
#         "passport_number": "A1234567"
#     })
#     assert response.status_code == 200
#     data = response.json()
#     assert data["passenger_name"] == "John"
#     assert data["passport_number"] == "A1234567"
#
# def test_overbooking():
#     flight = create_flight()
#     # Book 2 seats (max)
#     client.post(f"/flights/{flight['id']}/book", json={
#         "passenger_name": "John",
#         "passport_number": "A1234567"
#     })
#     client.post(f"/flights/{flight['id']}/book", json={
#         "passenger_name": "Jane",
#         "passport_number": "B1234567"
#     })
#     # Third booking should fail due to no seats left
#     response = client.post(f"/flights/{flight['id']}/book", json={
#         "passenger_name": "Mark",
#         "passport_number": "C1234567"
#     })
#     assert response.status_code == 400
#     assert response.json()["detail"] == "No available seats"
#
# def test_duplicate_passport():
#     flight = create_flight()
#     client.post(f"/flights/{flight['id']}/book", json={
#         "passenger_name": "John",
#         "passport_number": "A1234567"
#     })
#     # Attempt booking with same passport number again
#     response = client.post(f"/flights/{flight['id']}/book", json={
#         "passenger_name": "John Duplicate",
#         "passport_number": "A1234567"
#     })
#     assert response.status_code == 400
#     assert response.json()["detail"] == "Passport number already used"
#
# def test_invalid_passport_format():
#     flight = create_flight()
#     response = client.post(f"/flights/{flight['id']}/book", json={
#         "passenger_name": "Alice",
#         "passport_number": "123abc"  # invalid format
#     })
#     assert response.status_code == 422  # Validation error from Pydantic
#
# def test_cancel_booking():
#     flight = create_flight()
#     # Book a flight
#     book_resp = client.post(f"/flights/{flight['id']}/book", json={
#         "passenger_name": "John",
#         "passport_number": "A1234567"
#     })
#     booking_id = book_resp.json()["id"]
#     # Cancel booking
#     response = client.delete(f"/bookings/{booking_id}")
#     assert response.status_code == 200
#     assert response.json()["message"] == "Booking cancelled successfully"



import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from app.main import app
from app.database import Base, get_db

# Helper: create new in-memory DB and client for each test
def setup_test_db():
    SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL,
        connect_args={"check_same_thread": False},
        poolclass=StaticPool
    )
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base.metadata.create_all(bind=engine)

    # Override the get_db dependency to use this session
    def override_get_db():
        db = TestingSessionLocal()
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db
    client = TestClient(app)
    return client, engine

def teardown_test_db(engine):
    Base.metadata.drop_all(bind=engine)

# 1. Test flight creation
def test_create_flight():
    client, engine = setup_test_db()

    response = client.post("/flights/", json={
        "flight_number": "AI101",
        "airline": "Air India",
        "departure": "Delhi",
        "destination": "Mumbai",
        "departure_time": "2025-05-30T10:00:00",
        "total_seats": 2
    })
    assert response.status_code == 200
    assert response.json()["flight_number"] == "AI101"

    teardown_test_db(engine)


# 2. Test booking flight success
def test_book_flight_success():
    client, engine = setup_test_db()

    # Create flight first
    flight_resp = client.post("/flights/", json={
        "flight_number": "AI101",
        "airline": "Air India",
        "departure": "Delhi",
        "destination": "Mumbai",
        "departure_time": "2025-05-30T10:00:00",
        "total_seats": 2
    })
    flight_id = flight_resp.json()["id"]

    # Book seat
    book_resp = client.post(f"/flights/{flight_id}/book", json={
        "passenger_name": "John",
        "passport_number": "A1234567"
    })
    assert book_resp.status_code == 200
    assert book_resp.json()["passenger_name"] == "John"

    teardown_test_db(engine)


# 3. Test overbooking
def test_overbooking():
    client, engine = setup_test_db()

    # Create flight with 2 seats
    flight_resp = client.post("/flights/", json={
        "flight_number": "AI101",
        "airline": "Air India",
        "departure": "Delhi",
        "destination": "Mumbai",
        "departure_time": "2025-05-30T10:00:00",
        "total_seats": 2
    })
    flight_id = flight_resp.json()["id"]

    # Book 2 seats
    client.post(f"/flights/{flight_id}/book", json={
        "passenger_name": "John",
        "passport_number": "A1234567"
    })
    client.post(f"/flights/{flight_id}/book", json={
        "passenger_name": "Jane",
        "passport_number": "B1234567"
    })

    # Third booking should fail
    resp = client.post(f"/flights/{flight_id}/book", json={
        "passenger_name": "Mark",
        "passport_number": "C1234567"
    })
    assert resp.status_code == 400
    assert resp.json()["detail"] == "No available seats"

    teardown_test_db(engine)


# 4. Test duplicate passport booking
def test_duplicate_passport():
    client, engine = setup_test_db()

    # Create flight
    flight_resp = client.post("/flights/", json={
        "flight_number": "AI101",
        "airline": "Air India",
        "departure": "Delhi",
        "destination": "Mumbai",
        "departure_time": "2025-05-30T10:00:00",
        "total_seats": 2
    })
    flight_id = flight_resp.json()["id"]

    # Book seat with passport
    client.post(f"/flights/{flight_id}/book", json={
        "passenger_name": "John",
        "passport_number": "A1234567"
    })

    # Attempt duplicate passport
    resp = client.post(f"/flights/{flight_id}/book", json={
        "passenger_name": "John Duplicate",
        "passport_number": "A1234567"
    })
    assert resp.status_code == 400
    assert resp.json()["detail"] == "Passport number already used"

    teardown_test_db(engine)


# 5. Test invalid passport format (expect validation error)
def test_invalid_passport_format():
    client, engine = setup_test_db()

    # Create flight
    flight_resp = client.post("/flights/", json={
        "flight_number": "AI101",
        "airline": "Air India",
        "departure": "Delhi",
        "destination": "Mumbai",
        "departure_time": "2025-05-30T10:00:00",
        "total_seats": 2
    })
    flight_id = flight_resp.json()["id"]

    # Try booking with invalid passport
    resp = client.post(f"/flights/{flight_id}/book", json={
        "passenger_name": "Alice",
        "passport_number": "123abc"  # Invalid format
    })
    assert resp.status_code == 422  # Pydantic validation error

    teardown_test_db(engine)


# 6. Test cancelling a booking
def test_cancel_booking():
    client, engine = setup_test_db()

    # Create flight
    flight_resp = client.post("/flights/", json={
        "flight_number": "AI101",
        "airline": "Air India",
        "departure": "Delhi",
        "destination": "Mumbai",
        "departure_time": "2025-05-30T10:00:00",
        "total_seats": 2
    })
    flight_id = flight_resp.json()["id"]

    # Book seat
    booking_resp = client.post(f"/flights/{flight_id}/book", json={
        "passenger_name": "John",
        "passport_number": "A1234567"
    })
    booking_id = booking_resp.json()["id"]

    # Cancel booking
    cancel_resp = client.delete(f"/bookings/{booking_id}")
    assert cancel_resp.status_code == 200
    assert cancel_resp.json()["message"] == "Booking cancelled successfully"

    teardown_test_db(engine)
