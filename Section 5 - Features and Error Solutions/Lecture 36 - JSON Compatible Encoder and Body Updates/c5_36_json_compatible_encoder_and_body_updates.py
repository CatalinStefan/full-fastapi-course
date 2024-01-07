from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()

class HomeDesign(BaseModel):
    color_scheme: Optional[str] = Field(None, example="Warm")
    materials: Optional[str] = Field(None, example="Wood")

user_preferences = {}

@app.put("/update-design/{user_id}", response_model=HomeDesign)
async def update_design(user_id: int, design: HomeDesign):
    json_compatible_design = jsonable_encoder(design)

    user_preferences[user_id] = json_compatible_design

    return json_compatible_design
    