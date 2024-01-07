from fastapi import FastAPI


app = FastAPI()

trips = [
    {"id": 1, "destination": "Mars", "price": 10000},
    {"id": 2, "destination": "Moon", "price": 5000},
]

@app.get("/trips", tags=["Trips"], summary="list of trips",
    description="Retrieve a list of available interstellar trips with their details.")
async def list_trips(): 
    return trips

@app.post("/book-trip/{trip_id}", tags=["Booking"], summary="Book a trip",
    description="Book an interstellar trip by providing the trip ID.")
async def book_trip(trip_id:int):
    trip = next((trip for trip in trips if trip["id"] == trip_id), None)

    if trip is None:
        return {"error": "Trip not found"}

    return {"message": f"Trip to {trip['destination']} booked successfully!"}