from fastapi import FastAPI

from fmlwright.generator.run import run as build_generator
from fmlwright.core import data_sources
from pathlib import Path
import ast

app = FastAPI()

config_generator = data_sources.load_yaml(Path("./config/complete_floorplan.yaml"))
config_generator['settings']['input_shape'] = ast.literal_eval(config_generator['settings']['input_shape'])


generator = build_generator(config_generator)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get('/healthcheck', status_code=200)
async def healthcheck():
    return "Healthy"


@app.get('/predict')
async def predict():
    return generator.categories
