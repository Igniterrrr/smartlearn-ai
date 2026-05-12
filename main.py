
from fastapi import FastAPI, UploadFile, File
from app.routes.summarize import router as summarize_router

app = FastAPI(title="AI Learning System")

app.include_router(summarize_router)

@app.get("/")
def home():
    return {"message": "AI Learning System Backend Running"}

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    content = await file.read()
    return {
        "filename": file.filename,
        "size": len(content),
        "status": "uploaded"
    }
