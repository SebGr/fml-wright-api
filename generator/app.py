import ast
import io
from pathlib import Path
from typing import List

import numpy as np
from PIL import Image
from fastapi import FastAPI, File
from fmlwright.core import data_sources
from fmlwright.generator.run import run as build_generator
from pydantic import BaseModel

app = FastAPI()

config_generator = data_sources.load_yaml(Path("./config/complete_floorplan.yaml"))
config_generator['settings']['input_shape'] = ast.literal_eval(config_generator['settings']['input_shape'])


generator = build_generator(config_generator)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/categories")
async def categories():
    return generator.categories


@app.post("/generate_from_file")
async def generate_from_file(img_file: bytes = File(...)):
    image = Image.open(io.BytesIO(img_file))

    image = np.array(image)
    if image.shape[2] == 4:
        image = np.delete(image, -1, axis=-1)
    image = image / 255.0
    predictions = generator.predict(image, 1)
    preds = {}
    for key, value in predictions.items():
        if key[0] not in preds:
            preds[key[0]] = {}
        preds[key[0]][int(key[1])] = {
            "image": value.tolist(),
            "shape": value.shape
        }

    return preds


class GenerateRequest(BaseModel):
    image: List
    n_samples: int
    categories: List


@app.post("/generate")
async def generate(request: GenerateRequest):
    image = np.array(request.image)
    n_samples = request.n_samples
    if request.categories:
        predictions = generator.predict(image,
                                        n_samples=n_samples,
                                        categories=request["categories"])
    else:
        predictions = generator.predict(image, n_samples)

    preds = {}
    for key, value in predictions.items():
        if key[0] not in preds:
            preds[key[0]] = {}
        preds[key[0]][int(key[1])] = {
            "image": value.tolist(),
            "shape": value.shape
        }

    return preds
