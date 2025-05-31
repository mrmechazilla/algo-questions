from fastapi import FastAPI, File, UploadFile # type: ignore
from pathlib import Path

app = FastAPI()
UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

@app.post("/upload-json")
async def upload_json(file: UploadFile = File(...)):
    #if file.content_type != "application/json":
    #    raise HTTPException(status_code=400, detail="Only JSON files are allowed.")
    
    file_path = UPLOAD_DIR / file.filename
    with open(file_path, "wb") as buffer:
        while chunk := await file.read(1024):
            buffer.write(chunk)
    
    return {"message": f"File saved to {file_path}"}