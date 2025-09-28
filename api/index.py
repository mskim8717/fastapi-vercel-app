from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI(title="My FastAPI App", version="1.0.0")

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI on Vercel!"}

@app.get("/api/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id, "name": f"User {user_id}"}

@app.post("/api/items")
def create_item(item: dict):
    return {"item": item, "status": "created"}

# Vercel을 위한 핸들러
from mangum import Mangum
handler = Mangum(app)