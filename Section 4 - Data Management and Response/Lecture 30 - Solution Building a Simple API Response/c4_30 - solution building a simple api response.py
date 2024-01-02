from fastapi import FastAPI, HTTPException
from datetime import datetime


app = FastAPI()


# Define a GET route to calculate the number of days until the next birthday.
@app.get("/birthday/{date_of_birth}")
async def calculate_days(date_of_birth: str):

    try:
        # Attempt to convert the 'date_of_birth' string to a datetime object.       
        dob = datetime.fromisoformat(date_of_birth).date()

    except ValueError:
        # If the date format is incorrect, raise an HTTP 400 error with a descriptive message.
        raise HTTPException(status_code=400, detail="Invalid date format. Please use YYYY-MM-DD")

    
    # Get the current date.
    today = datetime.now().date()

    # Calculate the date of the next birthday.
    next_birthday = dob.replace(year=today.year)

    # If today's date is already past this year's birthday, calculate next year's birthday.
    if today > next_birthday:
        next_birthday = dob.replace(year=today.year + 1)

     # Calculate the number of days until the next birthday.
    days_until = (next_birthday - today).days

    # Return the number of days in a JSON response.
    return {"days_until_next_birthday": days_until}