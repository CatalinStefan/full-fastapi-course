from fastapi import FastAPI, File, UploadFile, Form 


app = FastAPI()


# Create a POST route to handle form uploads.
@app.post("/submit-form")
async def handle_form_upload(file: UploadFile = File(...), notes: str = Form(...)):
    
    # Read the contents of the uploaded file asynchronously.
    contents = await file.read()

    # Count the number of lines in the file's contents.
    num_lines = contents.decode("utf-8").count("\n") + 1

    # Calculate the file size by counting the number of bytes in 'contents'.
    file_size = len(contents)

    # Reset the file's pointer to the beginning after reading.
    await file.seek(0)

    # Return a JSON response containing details about the uploaded file and the notes.
    return {
        "file_name": file.filename,
        "file_size": file_size,
        "number_of_lines": num_lines,
        "notes": notes
    }