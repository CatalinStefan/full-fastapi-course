from fastapi import FastAPI


app = FastAPI()


# Define a GET route for fetching a joke.
@app.get("/jokes/")
def tell_joke(category: str):
    # It accepts a 'category' parameter of type string, which is expected to define the category of the joke.
    return {"joke": "Why did the programmer quit his job? He didn't get arrays."}