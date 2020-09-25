from typing import Dict

import numpy as np
from fastapi import APIRouter
from starlette.requests import Request

from app.models.generate import GeneratePayload

router = APIRouter()


@router.post("/generate")
async def generate(request: Request, generate_payload: GeneratePayload) -> Dict:
    """Generate floorplans based on input image.

    Args:
        request: request containing model.
        generate_payload: Payload, requires an image, n_samples, and categories (may be an empty list).

    Returns:
        Nested dictionary containing the categories, image number and images.
    """
    model = request.app.state.model

    image = np.array(generate_payload.image)
    n_samples = generate_payload.n_samples

    categories = generate_payload.categories
    if categories:
        predictions = model.predict(image, n_samples=n_samples, categories=categories)
    else:
        predictions = model.predict(image, n_samples)

    preds = {}
    for key, value in predictions.items():
        if key[0] not in preds:
            preds[key[0]] = {}
        preds[key[0]][int(key[1])] = {"image": value.tolist(), "shape": value.shape}

    return preds
