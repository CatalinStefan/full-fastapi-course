from fastapi import FastAPI, HTTPException
import logging


app = FastAPI()


@app.get("/item/{item_id}")
async def read_item(item_id: int):
    if item_id != 42:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": item_id}

logging.basicConfig(level=logging.INFO)

@app.get("/debug-item/{item_id}")
async def debug_item(item_id: int):
    logging.info(f"Request received for item_id: {item_id}")

    breakpoint()