from fastapi import FastAPI
from urllib.parse import urlparse

app = FastAPI()

@app.get("/api")
def read_api(request: str):
    query_string = urlparse(request).query
    return {"query_string": query_string}
