from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
import asyncio


app = FastAPI()


# Define a Pydantic model 'TimeCapsuleItem' for validating time capsule submission data.
class TimeCapsuleItem(BaseModel):
    email: EmailStr
    message: str
    send_date: datetime = Field(..., example="2023-12-31T00:00:00")


# Initialize a list to store time capsule items.
time_capsule_storage = []

# Create a POST route for submitting a time capsule item.
@app.post("/submit-time-capsule/")
async def submit_time_capsule(item: TimeCapsuleItem):
    time_capsule_storage.append(item)
    return {"message": "Time capsule item submitted successfully!"}

# Define an asynchronous function to check and send emails.
async def check_and_send_emails():
    while True:
        current_date = datetime.now()
        for item in time_capsule_storage:
            if item.send_date.date() == current_date.date():               
                print(f"Sending email to {item.email}: {item.message}")
        await asyncio.sleep(86400)  
