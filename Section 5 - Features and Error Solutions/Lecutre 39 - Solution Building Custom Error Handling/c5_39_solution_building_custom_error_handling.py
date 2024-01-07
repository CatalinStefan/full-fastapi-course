from fastapi import FastAPI, HTTPException, Request, status
from fastapi.responses import JSONResponse

app = FastAPI()

# Mock data: match tickets availability (0 = sold out)
match_tickets = {"Portugal vs Argentina": 0}

# Custom exception class for specific API errors
class CustomAPIException(Exception):
    def __init__(self, status_code: int, message: str):
        self.status_code = status_code
        self.message = message

# Handles responses for CustomAPIException
@app.exception_handler(CustomAPIException)
async def custom_api_exception_handler(request: Request, exc: CustomAPIException):
    return JSONResponse(status_code=exc.status_code, content={"message": exc.message})

# Endpoint to book a match ticket
@app.post("/book-match-ticket")
async def book_match_ticket(match: str):
    # Your code here: Validate match and ticket availability
    if match not in match_tickets:
        raise CustomAPIException(status.HTTP_422_UNPROCESSABLE_ENTITY, "Invalid booking request.")
    
    if match_tickets[match] == 0:
        raise CustomAPIException(status.HTTP_400_BAD_REQUEST, "Sorry, tickets for this match are sold out.")


    return {"message": f"Ticket for {match} booked successfully!"}
