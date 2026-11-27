from pydantic import BaseModel
from typing import Optional


class Item(BaseModel):
    task: Optional[str]
    description: Optional[str]
    done: Optional[bool]
    