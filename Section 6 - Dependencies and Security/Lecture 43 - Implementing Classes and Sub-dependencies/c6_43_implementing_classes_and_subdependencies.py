from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel


app = FastAPI()

class User(BaseModel):
    username: str
    password: str

users = {"max": "power", "charlie": "sun"}

class UserAuthenticator:
    
    def __init__(self, users_db):
        self.users_db = users_db

    def authenticate(self, username: str, password: str):

        if username in self.users_db and self.users_db[username] == password:
            return username
        
        raise HTTPException(status_code=401, detail="Invalid credentials")

authenticator = UserAuthenticator(users)

@app.post("/login")
async def login(user: User, username: str = Depends(authenticator.authenticate)):
    return {"message": f"Welcome back, {username}!"}