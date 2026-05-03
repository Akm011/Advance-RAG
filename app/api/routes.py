from fastapi import APIRouter
from app.models.request_models import QueryRequest
from app.models.response_models import QueryResponse
from app.services.query_service import handle_query

router = APIRouter()

@router.post("/query", response_model=QueryResponse)
def query_endpoint(request: QueryRequest):
    result = handle_query(request.query)
    return result