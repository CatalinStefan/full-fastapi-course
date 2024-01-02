from fastapi import FastAPI


app = FastAPI()


# Define a GET route to generate a greeting message.
@app.get("/greet/{name}")
async def greet(name: str):
    return {"message": f"Hello, {name}"}