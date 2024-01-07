from fastapi import FastAPI

# Create an instance of the FastAPI class
app = FastAPI()

# Define a route handler for the root URL ("/")
@app.get("/")
def read_root():
    # This function, 'read_root', is called when a GET request is made to the root URL.
    # It returns a JSON response containing a key-value pair.
    return {"hello": "world"}