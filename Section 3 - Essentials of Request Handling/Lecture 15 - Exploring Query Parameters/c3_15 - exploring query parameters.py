from fastapi import FastAPI, Query


app = FastAPI()

# Define a GET route for finding restaurants.
@app.get("/restaurants/")
async def find_restaurants(cuisine: str = Query(None), vegetarian: bool = Query(False)):
     # The function accepts two optional query parameters.
    return {"cuisine": cuisine, "vegetarian": vegetarian}