from fastapi import APIRouter


book_router = APIRouter()

# Sample data
books = [{"id": 1, "title": "A Hero's Welcome", "author": "Trent Locke"}]

@book_router.get("/books/")
async def get_books():
    return books

@book_router.post("/books/")
async def add_book(book_id: int, title: str, author: str):
    new_book = {"id": book_id, "title": title, "author": author}
    books.append(new_book)
    return new_book

