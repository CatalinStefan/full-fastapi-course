from fastapi import FastAPI, HTTPException
from typing import Dict


app = FastAPI()

trips = {"1": {"destination": "Mars", "available": True}, 
    "2": {"destination": "Moon", "available": False}}
bookings: Dict[str, str] = {}

@app.post("/book-trip/{trip_id}")
async def book_trip(trip_id: str):

    if trip_id not in trips:
        raise HTTPException(status_code=404, detail="Trip not found")
    
    if not trips[trip_id]["available"]:
        raise HTTPException(status_code=400, detail="Trip is not available")

    if trip_id in bookings:
        raise HTTPException(status_code=400, detail="Trip is already booked")

    bookings[trip_id] = "booked"
    return {"message": f"Trip to {trips[trip_id]['destination']} booked succesfully!"}