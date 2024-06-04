from pydantic import BaseModel

class Event(BaseModel):
    summary: str
    start: str
    end: str
    time_zone: str