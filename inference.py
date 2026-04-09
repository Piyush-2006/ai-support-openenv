from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API is running"}

@app.post("/reset")
def reset():
    return {"status": "reset successful"}

@app.post("/infer")
def infer():
    return {"result": "ok"}