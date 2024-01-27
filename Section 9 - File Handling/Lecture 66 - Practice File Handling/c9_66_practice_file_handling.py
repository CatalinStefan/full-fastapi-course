from fastapi import FastAPI, File, UploadFile, HTTPException
import os
import shutil
from fastapi.staticfiles import StaticFiles

app = FastAPI()

os.makedirs("static/uploaded_images", exist_ok=True)

@app.post("/upload-image/")
async def upload_image(file: UploadFile = File(...)):
    
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File is not an image.")

    file_path = f"static/uploaded_images/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"file_path": file_path}

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/images/")
async def list_images():
    image_directory = os.listdir("static/uploaded_images")
    image_urls = [f"/static/uploaded_images/{image}" for image in image_directory]
    return {"image_urls": image_urls}