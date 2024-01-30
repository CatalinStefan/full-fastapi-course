from fastapi import FastAPI, HTTPException


app = FastAPI()

books = {
    "1": {"title": "Our Time", "borrowed": False},
    "2": {"title": "Into the Fire", "borrowed": False},

}

@app.get("/borrow-book/{book_id}")
async def borrow_book(book_id: str):
    book = books.get(book_id)


    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    if book["borrowed"]:
        raise HTTPException(status_code=400, detail="Book is already borrowed")

    book["borrowed"] = True
    return {"message": f"You have successfully borrowed '{book['title']}"}