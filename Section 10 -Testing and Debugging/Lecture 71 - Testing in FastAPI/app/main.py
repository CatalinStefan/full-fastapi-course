from fastapi import FastAPI
from pydantic import BaseModel, Field


app = FastAPI()


class Item(BaseModel):
    title: str
    size: int = Field(..., gt=0)  

@app.get("/")
async def read_main():
    return {"message": "Hello World"}

@app.post("/items/")
async def create_item(item: Item):   
    return item
