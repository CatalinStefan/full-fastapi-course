from fastapi import FastAPI
from pydantic import BaseModel



app = FastAPI()


# Define a Pydantic model 'Person'.
class Person(BaseModel):
    name: str
    age: int

# Define another Pydantic model 'Family'.
class Family(BaseModel):
    parents: list[Person]
    children: list[Person]

# Create a POST route to create a family tree.
@app.post("/family-tree/")
async def create_family(family: Family):
    return family