from fastapi import FastAPI


app = FastAPI()

# Create a mock database of products.
products_db = [{"product_name": "Soap"}, {"product_name": "Shampoo"}, {"product_name": "Toothpaste"}, {"product_name": "Toilet Paper"}]

# Define a route to get a list of toiletry products.
@app.get("/toiletries/")
async def read_toiletries(offset: int = 0, range: int = 10):
    # The function returns a slice of the 'products_db' list.
    return products_db[offset : offset + range]

# Define a route in the FastAPI application for fetching details of a specific book.
@app.get("/books/{book_id}")
async def my_book(book_id: str, q = None):
    # It accepts 'book_id' as a mandatory path parameter of type string.
    # 'q' is an optional query parameter.

    # Check if the optional query parameter 'q' is present.
    if q:
        return {"book_id": book_id, "q": q}
    else:
        return {"book_id": book_id}