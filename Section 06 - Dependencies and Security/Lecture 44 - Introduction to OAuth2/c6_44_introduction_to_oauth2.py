from fastapi import FastAPI, Depends, HTTPException, status 
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

users = {"max": "power", "charlie": "sun"}

def verify_token(token: str):
    return token in users.keys()

@app.post("/token")
async def generate_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user_password = users.get((form_data.username))

    if user_password and form_data.password == user_password:
        return {"access_token": form_data.username, "token_type": "bearer"}

    raise HTTPException(
        status_code= status.HTTP_401_UNAUTHORIZED,
        detail= "Incorrect username or password",
        headers= {"WWW-Authenticate": "Bearer"}
    )

@app.get("/users/me")
async def read_users_me(token: str = Depends(oauth2_scheme)):

    if verify_token(token):
        return {"token": token}

    raise HTTPException(status_code=400, detail="Invalid token")