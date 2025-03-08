from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from auth import get_current_user
from models import Movie, Show
from database import get_db
from datetime import datetime

router = APIRouter()

@router.post("/movies/")
def add_movie(title: str, description: str, db: Session = Depends(get_db), user=Depends(get_current_user)):
    if not user.is_owner:
        raise HTTPException(status_code=403, detail="Only theater owners can add movies")
    movie = Movie(title=title, description=description)
    db.add(movie)
    db.commit()
    return {"message": "Movie added successfully!"}

@router.get("/movies/")
def get_movies(db: Session = Depends(get_db)):
    return db.query(Movie).all()
