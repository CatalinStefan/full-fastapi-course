from fastapi import FastAPI, Depends
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base
from sqlalchemy.future import select
from pydantic import BaseModel
from typing import List
from config import DB_USER, DB_PASSWORD


app = FastAPI()

DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@localhost/librarydb"

# Create an async engine instance 
async_engine = create_async_engine(DATABASE_URL, echo=True)

# Base class for SQLAlchemy models
Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String, index=True)

# Pydantic model for Book 
class BookSchema(BaseModel):
    id: int
    title: str
    author: str

# Dependency function for database session
async def get_db_session():
    async with AsyncSession(async_engine) as session:
        yield session

# Endpoint to create a new book
@app.post("/books/", response_model=BookSchema)
async def create_book(book_data: BookSchema, session: AsyncSession = Depends(get_db_session)):
    book = Book(title=book_data.title, author=book_data.author)
    session.add(book)
    await session.commit()
    await session.refresh(book)
    return book

# Endpoint to retrieve all books
@app.get("/books/", response_model=List[BookSchema])
async def get_books(session: AsyncSession = Depends(get_db_session)):
    result = await session.execute(select(Book))
    books = result.scalars().all()
    return [BookSchema(id=book.id, title=book.title, author=book.author) for book in books]