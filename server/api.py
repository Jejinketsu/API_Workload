from typing import Optional
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import FileResponse
from database.connectionToMySQL import DataBaseMySql

app = FastAPI()
db = DataBaseMySql()

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    print({"filename": file.filename})
    contents = await file.read()
    try:
        db.connect()
        db.insert(contents)
        db.disconnect()
    except:
        raise HTTPException(status_code=500)
        
    return {"filename": file.filename}
