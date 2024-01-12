from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel


app = FastAPI()

class User(BaseModel):
    username: str
    password: str

users = {"max": "power", "charlie": "sun"}

def authenticate_user(username: str, password: str):

    if username in users and users[username] == password:
        return username
    
    raise HTTPException(status_code=401, detail="Invalid credentials")

@app.post("/login")
async def login(user:User, username: str = Depends(authenticate_user)):
    return {"message": f"Welcome back, {username}!"}