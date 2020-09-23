import ast
import io
from pathlib import Path

import numpy as np
from PIL import Image
from fastapi import FastAPI, File
from fmlwright.core import data_sources
from fmlwright.generator.run import run as build_generator

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


@app.post("/predict_image")
async def predict_image(img_file: bytes = File(...)):
    image = Image.open(io.BytesIO(img_file))

    image = np.array(image)
    if image.shape[2] == 4:
        image = np.delete(image, -1, axis=-1)
    image = image / 255.0
    predictions = generator.predict(image, 1)
    preds = {}
    for key, value in predictions.items():
        preds[(key[0], int(key[1]))] = value.tostring()

    return list(preds.keys())
