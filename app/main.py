from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="RAG Policy API")

app.include_router(router, prefix="/api")

@app.get("/")
def health_check():
    return {"status": "ok"}