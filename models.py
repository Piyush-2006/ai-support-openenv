from pydantic import BaseModel

class Observation(BaseModel):
    message: str

class Action(BaseModel):
    category: str  # refund / complaint / query

class Reward(BaseModel):
    score: float