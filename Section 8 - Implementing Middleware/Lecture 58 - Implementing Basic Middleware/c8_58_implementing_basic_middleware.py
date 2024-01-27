from fastapi import FastAPI, Request
import time


app = FastAPI()

@app.middleware("http")
async def log_requests(request: Request, call_next):

    start_time = time.time()

    response = await call_next(request)

    duration = time.time() - start_time 

    print(f"Request:{request.method} {request.url} - Response Time: {duration:.2f} seconds")

    return response 

@app.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI ecosystem"}