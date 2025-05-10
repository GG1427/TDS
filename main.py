from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import json
from urllib.parse import urlparse, parse_qs

app = FastAPI()

# Add CORS middleware to the app
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins. You can restrict this to specific domains like ["https://yourfrontend.com"]
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

@app.get("/api")
async def read_api(request: Request):
    # Get the full URL from the request
    query_string = urlparse(str(request.url)).query
    
    # Parse the query string into a dictionary
    query_params = parse_qs(query_string)

    # Check if 'name' query parameter exists and has at least two values
    names = query_params.get('name', [])
    if len(names) < 2:
        raise HTTPException(status_code=400, detail="At least two 'name' parameters are required.")

    # Open the JSON file and load the data
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="data.json file not found.")
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Error decoding JSON from data.json file.")

    # Initialize an empty list to store marks
    li = []
    
    # Loop through the names and find the corresponding marks in the data
    for name in names:
        # Search for the name in the data (data is a list of dictionaries)
        found = False
        for entry in data:
            if entry['name'] == name:
                li.append(entry['marks'])
                found = True
                break  # Exit loop once the matching entry is found
        if not found:
            li.append(None)  # If the name is not found, append None

    return {"marks": li}
