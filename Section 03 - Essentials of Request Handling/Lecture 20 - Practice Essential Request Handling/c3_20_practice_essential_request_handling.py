from fastapi import FastAPI
from pydantic import BaseModel, Field
from datetime import date



app = FastAPI()


# Define a Pydantic model 'Event'.
class Event(BaseModel):
    name: str = Field(..., min_length=1)
    event_date: date
    type: str = Field(..., min_length=1)
    location: str


# Initialize an empty list to store events.
events = []

# Create a POST route to add a new event.
@app.post("/add-event/")
async def add_event(event: Event):
    events.append(event.dict())
    return {"message": "Event added successfully!"}

# Create a GET route to view events, with optional filtering parameters.
@app.get("/view-events/")
async def view_events(event_date: date = None, type: str = None, location: str = None):
    filtered_events = [event for event in events if 
            	(event_date is None or event['event_date'] == event_date) and
            	(type is None or event['type'] == type) and
            	(location is None or event['location'] == location)]
    return filtered_events