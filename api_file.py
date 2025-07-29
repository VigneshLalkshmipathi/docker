# app.py
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI on EC2 + Docker!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)
