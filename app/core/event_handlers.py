from fastapi import FastAPI
from fmlwright.core import data_sources
from fmlwright.generator.run import run as build_generator
import ast
from pathlib import Path
import logging

logger = logging.getLogger("__name__")


def _startup_model(app: FastAPI) -> None:
    config_generator = data_sources.load_yaml(Path("./app/config.yaml"))
    config_generator['settings']['input_shape'] = ast.literal_eval(config_generator['settings']['input_shape'])

    logger.info("Building Generator.")
    generator = build_generator(config_generator)

    app.state.model = generator


def _shutdown_model(app: FastAPI) -> None:
    app.state.model = None


def start_app_handler(app: FastAPI) -> FastAPI:
    def startup() -> None:
        logger.info("Starting up handler.")
        _startup_model(app)
    return startup


def stop_app_handler(app: FastAPI) -> FastAPI:
    def shutdown() -> None:
        logger.info("Shutting down handler.")
        _shutdown_model(app)
    return shutdown
