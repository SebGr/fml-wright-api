from typing import List

from fastapi import APIRouter
from starlette.requests import Request

router = APIRouter()


@router.get("/categories")
async def categories(request: Request) -> List:
    """Show the categories that the loaded interface has.

    Args:
        request: request containing model.

    Returns:
        List of model categories present.
    """
    return request.app.state.model.categories
