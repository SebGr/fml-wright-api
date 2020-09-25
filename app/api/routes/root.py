from typing import Dict

from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def root() -> Dict:
    """Root directory.

    Returns:
        Message stating hello world.
    """
    return {"message": "Hello World"}
