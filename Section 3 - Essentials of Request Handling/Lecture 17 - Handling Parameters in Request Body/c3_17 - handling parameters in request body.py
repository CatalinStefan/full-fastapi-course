from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


# Define a Pydantic model 'Gift' for data validation.
class Gift(BaseModel):
    # Define fields for the 'Gift' model.
    type: str
    color: str
    size: str

# Create a POST route to receive a gift.
@app.post("/receive-gift/")
async def receive_gift(gift: Gift):
    return {"detail": f"Received a {gift.size} {gift.color} {gift.type}"}