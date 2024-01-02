from fastapi import FastAPI, HTTPException
from enum import Enum
from pathlib import Path

app = FastAPI()

# The route is '/products/{product_id}', where 'product_id' is a path parameter.
@app.get("/products/{product_id}")
async def read_product(product_id):
    # This function 'read_product' is triggered when a GET request is made to the '/products/{product_id}' URL.
    # It returns a JSON response with the product_id.
    return {"product_id": product_id}

# Define a similar route with type annotation for the path parameter.
# This time, 'product_id' is explicitly defined as an integer.
@app.get("/products/{product_id}")
async def read_product(product_id: int):
    return {"product_id": product_id}

# Define a route to get data for the current user.
@app.get("/users/me")
async def read_current_user():
    return {"user_id": "the data for the current user"}

# Define a route to get data for a user by their user_id.
@app.get("/users/{user_id}")
async def read_user(user_id: str):
    # Placing this route after '/users/me' prevents 'me' from being
    # interpreted as a user_id, maintaining the correct functionality of both routes.
    return {"user_id": user_id}

# Define a subclass of Enum to represent different types of devices.
class DeviceType(str, Enum):
    smartphone = "smartphone"
    tablet = "tablet"
    laptop = "laptop"

# Create a route in the FastAPI app to get information about a specific device type.
@app.get("/devices/{device_type}")
async def get_device(device_type: DeviceType):
    return {"device_type": device_type}

# Define a route in the FastAPI application to read and return the content of a document.
@app.get("/docs/{file_path:path}")
async def read_document(file_path: str):
    # Create a Path object from the 'docs' directory, joining it with the 'file_path' from the URL.    
    file_location = Path("docs") / file_path
    # If not, raise an HTTPException with a 404 status code indicating "file not found".
    if not file_location.exists() or not file_location.is_file():
        raise HTTPException(status_code= 404, detail = "file not found")

    # Open the file for reading ('r') and read its content. 
    with open(file_location, "r") as file:
        content = file.read()
    # Return the content of the file in a JSON response.
    return {"content": content}