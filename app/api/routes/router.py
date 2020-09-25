from fastapi import APIRouter

from app.api.routes import categories, root, generate_from_file, generate

api_router = APIRouter()
api_router.include_router(categories.router)
api_router.include_router(root.router)
api_router.include_router(generate_from_file.router)
api_router.include_router(generate.router)
