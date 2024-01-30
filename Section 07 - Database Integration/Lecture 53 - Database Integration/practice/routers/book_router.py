from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from practice import crud, models, schemas
from practice.database import SessionLocal



book_router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@book_router.get("/books/", response_model=list[schemas.Book])
async def get_books(db: Session = Depends(get_db)):
    return crud.get_books(db)

@book_router.post("/books/", response_model=schemas.Book)
async def add_book(book:schemas.BookCreate, db:Session=Depends(get_db)):
    return crud.create_book(db, book)


