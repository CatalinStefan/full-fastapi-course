from fastapi import FastAPI, Depends, HTTPException, status 
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from datetime import datetime, timedelta


app = FastAPI()


SECRET_KEY = "your_secret_key_here"
ALGORITHM = "HS256" 
ACCESS_TOKEN_EXPIRE_MINUTES = 30 

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

users = {"max": "power", "charlie": "sun"}

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes = 15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

@app.post('/token')
async def generate_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user_password = users.get(form_data.username)
    if user_password and form_data.password == user_password:
        token_data = {"sub": form_data.username}
        access_token = create_access_token(data=token_data, expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
        return {"access_token": access_token, "token_type": "bearer"}
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail= "Incorrect username or password",
        headers = {"WWW-Authenticate": "Bearer"},
    )

@app.get("/users/me")
async def read_users_me(token: str = Depends(oauth2_scheme)):
    try: 
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(
                status_code=400, detail="Invalid Credentials"
            )
    except JWTError:
        raise HTTPException(status_code=400, detail="Invalid Token")
    return {"username": username}