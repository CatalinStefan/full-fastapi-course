from fastapi import FastAPI, File, UploadFile, HTTPException
from typing import List
import shutil
import os 

app = FastAPI()


ALLOWED_FILE_TYPES = {"jpg", "jpeg", "png", "gif", "pdf"}

def is_file_type_allowed(filename: str) -> bool:
    return filename.split(".")[-1].lower() in ALLOWED_FILE_TYPES

@app.post("/uploadfiles")
async def create_upload_files(files: List[UploadFile] = File(...)): 
    saved_files = []
    for file in files: 
        if not is_file_type_allowed(file.filename):
            raise HTTPException(status_code=400, detail=f"File type not allowed: {file.filename}")
        
        try:
            with open(f"temp_{file.filename}", "wb") as buffer: 
                shutil.copyfileobj(file.file, buffer)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error saving file:{e}")

        try:
            os.rename(f"temp_{file.filename}", f"permanent_{file.filename}")
            saved_files.append(f"permanent_{file.filename}")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error processing file:{e}")
        
        await file.close()

    return {"message": "Files successfully uploaded", "saved_files": saved_files}