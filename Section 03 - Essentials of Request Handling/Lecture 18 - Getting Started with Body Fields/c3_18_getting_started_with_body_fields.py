from fastapi import FastAPI
from pydantic import BaseModel, Field



app = FastAPI()



# Define a Pydantic model 'Traveler' for data validation.
class Traveler(BaseModel):
    # Define the 'name' field as a string.
    name: str = Field(..., example="John Mark")
    # Define 'passport_number' with validation criteria
    passport_number: str = Field(..., min_length=9, max_length=9)
    destination: str

# Create a POST route to process a traveler's arrival.
@app.post("/arrival/")
async def process_arrival(traveler: Traveler):
    return {"message": f"Welcome, {traveler.name}, to {traveler.destination}"}