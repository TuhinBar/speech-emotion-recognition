from pydantic import BaseModel

# Model for speech emotion recognition
class SER(BaseModel):
    emotion: str
    confidence: float

