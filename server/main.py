from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from pathlib import Path
import uuid
import io

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload_csv/")
async def upload_csv(file: UploadFile = File(...)):
    contents = await file.read()
    df = pd.read_csv(io.StringIO(contents.decode("utf-8")))
    filename = f"{uuid.uuid4().hex}.csv"
    path = Path("saved") / filename
    path.parent.mkdir(exist_ok=True)
    df.to_csv(path, index=False)

    return {"status": "saved", "filename": filename}