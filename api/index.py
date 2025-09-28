from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI on Vercel!"}

@app.get("/api/test")
def test():
    return {"status": "working", "message": "API is functioning properly"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

# Vercel을 위한 핸들러 설정
from mangum import Mangum

# 이 방식으로 수정
handler = Mangum(app, lifespan="off")