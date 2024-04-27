import time
from pydantic import BaseModel
from typing import Dict, List


class Step(BaseModel):
    position: int
    file_name: str
    description: str
    marker: Dict[str, str]


class Tutorial(BaseModel):
    name: str
    created_date_time: str
    steps: List[Step]
