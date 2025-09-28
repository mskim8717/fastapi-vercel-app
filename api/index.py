# api/index.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI!"}

@app.get("/api/test")
def test():
    return {"status": "working"}

# Vercel 핸들러
from mangum import Mangum
handler = Mangum(app, lifespan="off")