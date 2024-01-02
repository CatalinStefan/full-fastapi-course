from fastapi import FastAPI, HTTPException
from datetime import date
from typing import Optional

app = FastAPI()


# Initialize a list to represent a fake database of events.
events_db = [
    {"event_id": 1, "name": "Tech Conference", "date": "2024-12-01"},
    {"event_id": 2, "name": "Movie Premiere", "date": "2024-12-15"},
    {"event_id": 3, "name": "Musical Festival", "date": "2024-12-20"}
]

# Create a GET route for fetching details of a specific event based on its ID.
@app.get("/events/{event_id}")
async def read_event(event_id: int, start_date: Optional[date] = None):
    # Find the event in the 'events_db' list by matching the 'event_id'.
    # If no event matches, 'next' returns None.
    event = next((event for event in events_db if event["event_id"] == event_id), None)

    # If the event is not found, raise an HTTP 404 error.
    if not event:
        raise HTTPException(status_code = 404, detail = "Event not found")
    
    # If 'start_date' is provided, compare it with the event's date.
    if start_date and date.fromisoformat(event["date"]) < start_date:
        return {"message": "No events on or after the start date."}

    return event