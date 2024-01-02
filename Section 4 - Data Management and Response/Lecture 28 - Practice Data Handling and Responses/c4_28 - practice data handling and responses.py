from fastapi import FastAPI, Query 
from typing import Optional
from datetime import date
from pydantic import BaseModel


app = FastAPI()


# Define a Pydantic model 'Book'.
class Book(BaseModel):
    title: str
    price: float
    publication_date: Optional[date] = None

# Create a POST route to create a new book.
@app.post("/books/")
async def create_book(book: Book):
    return {"message": "Book created Successfully", "book": book}

# Create a GET route to read books, with optional search functionality.
@app.get("/books/")
async def read_books(q: Optional[str] = Query(None, min_length=3, max_length=50)):
     
    # A fake database (list of dictionaries) representing books.
    fake_db = {"title": "Book 1"}, {"title": "Book 2"}
    
    # If the 'q' parameter is provided, perform a search in the fake database.
    if q: 
        result = filter(lambda book: q.lower() in book["title"].lower(), fake_db)
        
        # Return the search query and the filtered result as a list.
        return {"search": q, "result": list(result)}
    
    # If no search query is provided, return all books.
    return {"books": fake_db}