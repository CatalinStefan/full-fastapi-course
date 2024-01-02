from fastapi import FastAPI
from pydantic import BaseModel, Field


app = FastAPI()


# Define a Pydantic model 'User' for data validation.
class User(BaseModel):
    # Define a 'username' field with validation criterias.
    username: str = Field(min_length=5, max_length=10, pattern="^[a-zA-Z0-9]+$")

# Create a POST route to create a new user.
@app.post("/create-user/")
async def create_user(user: User):
    return {"username": user.username}