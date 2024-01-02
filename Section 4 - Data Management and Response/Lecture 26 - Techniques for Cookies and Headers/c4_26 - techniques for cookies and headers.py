from fastapi import FastAPI, Response, Request

app = FastAPI()



# Initialize a list to represent a mock database of items.
items = [
    {"id": 1, "name": "item1", "category": "Books"},
    {"id": 2, "name": "item2", "category": "Electronics"},
    {"id": 3, "name": "item3", "category": "Clothing"}
]

# Create a GET route for fetching items.
@app.get("/items/")
async def read_items(request: Request, response: Response):
    # Retrieve the user's preference from the request cookies.
    user_preference = request.cookies.get('preference')

    # Set a custom header in the response.
    response.headers["Custom-Header"] = "Value"
   
    # If the user has a preference, filter the items by the user's preferred category.
    if user_preference:
        filtered_items = [item for item in items if item["category"] == user_preference]
        return {"items": filtered_items}
    
    # If no preference is specified, return all items.
    return {"items": items}