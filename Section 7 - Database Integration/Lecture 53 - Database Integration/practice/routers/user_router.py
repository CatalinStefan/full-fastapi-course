from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from practice import crud, models, schemas
from practice.database import SessionLocal

user_router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@user_router.get("/users/", response_model=list[schemas.User])
async def get_users(db: Session = Depends(get_db)):
    return crud.get_users(db)

@user_router.post("/users/", response_model=schemas.User)
async def add_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)


