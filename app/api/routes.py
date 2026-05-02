from fastapi import APIRouter
from app.services.query_service import handle_query
from app.models.request_models import QueryRequest

router = APIRouter()

@router.post("/query")
async def query_endpoint(request: QueryRequest):
    response = handle_query(request.query)
    return {"answer": response}