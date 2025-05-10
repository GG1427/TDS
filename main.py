from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root(name: str = None):
    if name:
        return {"name": name}
    return {"message": "Hello, World! Coming to you, from main.py"}
