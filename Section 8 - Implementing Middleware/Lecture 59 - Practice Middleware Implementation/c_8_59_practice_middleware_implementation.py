from fastapi import FastAPI, Request
import time

app = FastAPI()

@app.middleware("http")
async def log_client_ip(request: Request, call_next):

    client_ip = request.client.host
    print(f"Client IP: {client_ip}")

    start_time = time.time()

    response = await call_next(request)

    process_time = time.time() - start_time
   
    print(f"Request processed in {process_time:.2f} seconds")

    return response

@app.on_event("startup")
async def startup_event():

    print("Application startup: Preparing Middleware...")

@app.get("/")
async def read_root():

    return {"message": "Explorer Middleware in FastAPI ecosystem"}