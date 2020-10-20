from typing import Optional
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import FileResponse
from database.connectionToMySQL import DataBaseMySql
from database.connectionToPostgres import DataBasePostGres

app = FastAPI()
db_mysql = DataBaseMySql()
db_postgres = DataBasePostGres()

@app.post("/uploadfile_mysql/")
async def save_archive_in_mysql(file: UploadFile = File(...)):
    print({"filename": file.filename})
    contents = await file.read()
    try:
        db_mysql.connect()
        db_mysql.insert(contents)
        db_mysql.disconnect()
    except:
        raise HTTPException(status_code=500)
        
    return {"filename": file.filename}

@app.post("/uploadfile_postgres/")
async def save_archive_in_postgres(file: UploadFile = File(...)):
    print({"filename": file.filename})
    contents = await file.read()
    try:
        db_postgres.connect()
        db_postgres.insert(contents)
        db_postgres.disconnect()
    except:
        raise HTTPException(status_code=500)
        
    return {"filename": file.filename}