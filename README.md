
# ✈️ Flight Booking System

This is a full-stack **Flight Ticket Booking System** developed as part of a coding challenge. The system allows users to view available flights, book flight tickets, and cancel them. It also includes a generated Python SDK and setup/execution scripts.

---

## 📁 Project Structure

```
flight-booking-system/
│
├── backend/
│   ├── app/
│   │   ├── main.py           # FastAPI app entry point
│   │   ├── models.py         # SQLAlchemy models
│   │   ├── schemas.py        # Pydantic schemas
│   │   ├── database.py       # DB connection & initialization
│   │   ├── crud.py           # CRUD operations
│   │   └── routers/
│   │       └── flights.py    # API endpoints for flights
│   ├── tests/
│   │   └── test_main.py      # Backend unit tests
│   └── requirements.txt      # Python dependencies
│
├── frontend/
│   └── [React App Structure] # Displays flights & booking forms
│
├── sdk/
│   └── [Generated via OpenAPI] # Python SDK using OpenAPI Generator
│
├── scripts/
│   ├── setup.sh / setup.ps1  # Project setup (venv, deps)
│   ├── run.sh / run.ps1      # Launch backend & frontend
│
├── README.md
└── .env                      # Environment configs (DB, secrets)
```

---

## 🚀 Features

### Backend (FastAPI + SQLAlchemy)
- Add new flights
- Book and cancel tickets
- Prevent overbooking
- Validate passport numbers
- Expose OpenAPI spec at `/openapi.json`
- Unit tests for flight management

### Frontend (ReactJS)
- View available flights
- Book a ticket using a form
- Cancel bookings
- Display error/success messages

### Python SDK
- Generated via OpenAPI Generator
- Functions include:
  - `add_flight()`
  - `book_ticket()`
  - `cancel_booking()`
  - `list_flights()` / `get_flight_by_id()`

### Automation Scripts
- Setup and execution scripts available for both Linux/Mac and Windows

---

## ⚙️ Setup Instructions

### 1. Bash (Linux/macOS)

```bash
#!/bin/bash

echo "🔧 Creating Python virtual environment..."
python3 -m venv venv
source venv/bin/activate

echo "📦 Installing backend dependencies..."
pip install -r backend/requirements.txt

echo "📦 Installing frontend dependencies..."
cd frontend
npm install
cd ..

echo "✅ Setup complete."
```

### 2. PowerShell (Windows)

```powershell
Write-Host "🔧 Creating Python virtual environment..."
python -m venv venv

Write-Host "🟢 Activating virtual environment..."
.\venv\Scripts\Activate.ps1

Write-Host "📦 Installing backend dependencies..."
pip install -r backend\requirements.txt

Write-Host "📦 Installing frontend dependencies..."
Set-Location -Path frontend
npm install
Set-Location -Path ..

Write-Host "✅ Setup complete."
```

---

## 🏃 Execution Scripts

### Bash (run.sh)

```bash
#!/bin/bash

echo "🚀 Starting FastAPI backend..."
cd backend/app
uvicorn main:app --host 0.0.0.0 --port 8000 &
cd ../../

echo "🌐 Starting React frontend..."
cd frontend
npm run dev
```

### PowerShell (run.ps1)

```powershell
Write-Host "🚀 Starting FastAPI backend..."
Set-Location -Path backend\app
Start-Process -NoNewWindow uvicorn main:app --host 0.0.0.0 --port 8000
Set-Location -Path ../..

Write-Host "🌐 Starting React frontend..."
Set-Location -Path frontend
npm run dev
```

---

## 🌐 Deployed Links

- Backend (FastAPI): [https://aumne-ai-4.onrender.com](https://aumne-ai-4.onrender.com)
- Frontend (ReactJS): [https://aumne-fronten.vercel.app/](https://aumne-fronten.vercel.app/)

---

## ✅ Completion Checklist

- [x] Backend API with all core features
- [x] ReactJS client with UI for booking/canceling
- [x] Python SDK via OpenAPI
- [x] Scripts for setup and execution
- [x] Unit tests
- [x] Deployed apps

---

## 📬 Bonus Feature Ideas
- Real-time seat updates via WebSockets
- Email notifications for bookings/reminders
- User authentication and session management

---

## 🧪 Testing

To run backend unit tests:
```bash
cd backend
pytest
```

---

## 📄 License

This project is for demonstration and evaluation purposes.
