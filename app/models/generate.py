from typing import List

from pydantic import BaseModel


class GeneratePayload(BaseModel):
    image: List
    n_samples: int
    categories: List
