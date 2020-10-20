from typing import Optional
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/downloadfile/{filename}")
async def download_file(filename: str):
    return FileResponse(filename)

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    print({"filename": file.filename})
    new_file = open(file.filename, 'wb')
    contents = await file.read()
    new_file.write(contents)
    new_file.close()
    return {"filename": file.filename}
