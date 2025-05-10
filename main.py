from fastapi import FastAPI, Request
from urllib.parse import urlparse

app = FastAPI()

@app.get("/api")
async def read_api(request: Request):
    # Get the full URL from the request
    query_string = urlparse(str(request.url)).query
    return {"query_string": query_string}
