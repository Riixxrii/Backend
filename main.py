from fastapi import FastAPI
from database import engine, Base
from routers import users, movie, bookings

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(movie.router, prefix="/movies", tags=["Movies"])
app.include_router(bookings.router, prefix="/bookings", tags=["Bookings"])

@app.get("/")
def root():
    return {"message": "Welcome to the Movie Booking API!"}
