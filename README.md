# Backend

Movie Ticket Booking Backend (FastAPI)

🎬 Project Overview

This is a backend system for movie ticket booking, built using FastAPI. It supports dynamic pricing based on demand and time, user authentication, and theater management.

🚀 Features

🔑 Authentication (Level 0)

User Registration & Login

JWT-based Authentication

🎟 Movie & Show Management (Level 1)

User: View available movies & book tickets

Theater Owner: Manage shows, set base prices, and view bookings

📅 Ticket Booking System (Level 1)

Users can book seats for a show

Users can view past bookings

🛠 Tech Stack

FastAPI - Web framework

SQLAlchemy - ORM for database interactions

SQLite / PostgreSQL - Database

JWT (PyJWT) - Authentication

Uvicorn - ASGI server

Pydantic - Data validation

🔧 Installation & Setup

1️⃣ Clone the Repository
git clone https://github.com/your-repo/movie-ticket-booking.git
cd movie-ticket-booking

2️⃣ Set Up Virtual Environment
python -m venv .venv
source .venv/bin/activate   # MacOS/Linux
.venv\Scripts\activate    # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run Migrations (if using a database)
alembic upgrade head

5️⃣ Start the Server
uvicorn main:app --reload

📩 API Documentation

Once the server is running, visit:
http://127.0.0.1:8000/docs
for interactive Swagger UI.

📜 Postman Collection

Postman API collections must be shared via a Postman group invite link for all levels implemented.

🏗 Future Enhancements

Payment integration

Seat selection feature

Discount & promotional codes

Admin panel for managing theaters


