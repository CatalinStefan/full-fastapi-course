from fastapi import FastAPI



app = FastAPI()

# Define a GET route for fetching book details based on the title.
@app.get("/books/{title}")
def read_book(title: str, author: str = None, genre: str = None):
    # It takes 'title' as a mandatory path parameter of type string.    
    # 'author' and 'genre' are optional query parameters.
    return {"title": title, "author": author, "genre": genre}
