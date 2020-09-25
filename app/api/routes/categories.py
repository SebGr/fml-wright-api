from fastapi import APIRouter
from starlette.requests import Request

router = APIRouter()


@router.get("/categories")
async def categories(request: Request):
    return request.app.state.model.categories
