import datetime
import shutil
import uuid
from pathlib import Path
import uvicorn
from fastapi import FastAPI, UploadFile, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

from src.database import insert_history, get_history
from src.inference import classify_image

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory="templates")

UPLOAD_DIR = Path("static/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    print(f'HOme Page')
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/classify", response_class=HTMLResponse)
async def classify_page(request: Request):
    return templates.TemplateResponse("classify.html", {"request": request})

@app.post("/classify", response_class=HTMLResponse)
async def classify(request: Request, file: UploadFile):
    if not file.filename:
        raise HTTPException(status_code=400, detail="No file uploaded")

    try:
        unique_filename = f"{uuid.uuid4()}_{file.filename}"
        file_path = UPLOAD_DIR / unique_filename
        with file_path.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        result = classify_image(file_path)
        
        timestamp = datetime.datetime.now()
        insert_history(str(file_path), result, timestamp)

        return templates.TemplateResponse("classify.html", {
            "request": request,
            "result": result,
            "file_url": f"/static/uploads/{unique_filename}"
        })

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing file: {str(e)}")

@app.get("/history", response_class=HTMLResponse)
async def history_page(request: Request):
    try:
        history = get_history()
        print(f"History: {history}")
        return templates.TemplateResponse("history.html", {"request": request, "history": history})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching history: {str(e)}")

if __name__ == '__main__':
    uvicorn.run("main:app", host='localhost', port=5000, reload=True)
