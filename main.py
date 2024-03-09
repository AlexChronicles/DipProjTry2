from fastapi import FastAPI

app = FastAPI()

@app.get("/Hello")
def index():
    return {"details": "Hello World"}