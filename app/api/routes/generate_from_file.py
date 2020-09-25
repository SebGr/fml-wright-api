import io
from typing import Dict

import numpy as np
from PIL import Image
from fastapi import File, APIRouter
from starlette.requests import Request

router = APIRouter()


@router.post("/generate_from_file")
async def generate_from_file(request: Request, img_file: bytes = File(...)) -> Dict:
    """Generate an image from an input file.

    Args:
        request: request containing model.
        img_file: image file with input image.

    Returns:
        Nested dictionary containing the categories, image number and images.
    """
    model = request.app.state.model
    image = Image.open(io.BytesIO(img_file))

    image = np.array(image)
    if image.shape[2] == 4:
        image = np.delete(image, -1, axis=-1)
    image = image / 255.0
    predictions = model.predict(image, 1)
    preds = {}
    for key, value in predictions.items():
        if key[0] not in preds:
            preds[key[0]] = {}
        preds[key[0]][int(key[1])] = {"image": value.tolist(), "shape": value.shape}

    return preds
