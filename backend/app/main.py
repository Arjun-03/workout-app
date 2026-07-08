from fastapi import FastAPI

from app.api.v1 import auth

app = FastAPI()

app.include_router(auth.router)


@app.get("/")
def read_root():
    return {"status": "ok", "message": "Workout app is alive"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}