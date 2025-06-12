from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import json
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Payload(BaseModel):
    question: str
    image: Optional[List[str]] = None

@app.post("/api")
async def save_payload(data: Payload):
    entry = {"question": data.question, "image": data.image or []}
    os.makedirs("data", exist_ok=True)
    with open("data/requests.json", "w") as f:
        f.write(json.dumps(entry) + "\n")
    return {"status": "saved"}
