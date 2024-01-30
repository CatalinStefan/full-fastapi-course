from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel


app = FastAPI()

class SpacecraftDetails(BaseModel):
    name: str
    capacity: int

@app.get("/spacecraft/{name}")
async def get_spacecraft(name: str):

    spacecraft = SpacecraftDetails(name=name, capacity=200)

    json_compatible_spacecraft = jsonable_encoder(spacecraft)

    return json_compatible_spacecraft