from fastapi import FastAPI, File, UploadFile, HTTPException
import os
import shutil
import datetime


app = FastAPI()

PHOTO_DIR = "uploaded_photos"
os.makedirs(PHOTO_DIR, exist_ok = True)

@app.post("/upload-photo/")
async def upload_photo(file: UploadFile = File(...)):

    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Not an image file")

    file_path = os.path.join(PHOTO_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"filename": file.filename}

@app.get("/photos/")
def list_photos():

    files = os.listdir(PHOTO_DIR)
    categorized_photos = {}

    for file in files:

        file_date = datetime.datetime.fromtimestamp(os.path.getctime(os.path.join(PHOTO_DIR, file)))
        date_str = file_date.strftime("%Y-%m-%d")

        if date_str not in categorized_photos:
            categorized_photos[date_str] = []
        categorized_photos[date_str].append(file)

    return categorized_photos

@app.delete("/delete-photo/{filename}")
def delete_photo(filename: str):

    file_path = os.path.join(PHOTO_DIR, filename)

    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="file not found")

    os.remove(file_path)

    return {"message": "Photo deleted successfully"}