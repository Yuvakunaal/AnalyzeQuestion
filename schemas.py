from pydantic import BaseModel
from typing import List

class ProblemRequest(BaseModel):
    text: str

class ProblemResponse(BaseModel):
    patterns: List[str]
    difficulty: str
    approach: List[str]
