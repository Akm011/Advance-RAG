from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Project Aegis API")

app.include_router(router)