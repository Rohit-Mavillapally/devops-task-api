
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "My DevOps project is running!"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/tasks")
def get_tasks():
    return [
        {"id": 1, "task": "Learn Linux"},
        {"id": 2, "task": "Learn Docker"}
    ]


@app.get("/version")
def get_version():
    return {"version": "1.0.0"}

