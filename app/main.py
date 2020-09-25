from fastapi import FastAPI
from app.core.logging import create_logger
from app.core.event_handlers import (
    start_app_handler,
    stop_app_handler
)
from app.api.routes.router import api_router


def create_app() -> FastAPI:
    logger = create_logger()

    logger.info("Creating app.")
    application = FastAPI()
    application.include_router(api_router)

    application.add_event_handler("startup", start_app_handler(application))
    application.add_event_handler("shutdown", stop_app_handler(application))

    logger.info("Succesfully created app.")
    return application


app = create_app()
