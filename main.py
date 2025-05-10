from fastapi import FastAPI, Request, json
from urllib.parse import urlparse

app = FastAPI()

@app.get("/api")
async def read_api(request: Request):
    # Get the full URL from the request
    query_string = urlparse(str(request.url)).query
    with open("data.json", "r") as file:
        data = json.load(file)
    name1 = query_string.split("&")[0].split("=")[1]
    name2 = query_string.split("&")[1].split("=")[1]
    li = []
    li.append(data[name1])
    li.append(data[name2])
    
    return {"marks": li}
