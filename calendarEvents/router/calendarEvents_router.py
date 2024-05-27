from fastapi import APIRouter
from calendarEvents.models import calendarEventsModel
from calendarEvents.infrastructure import calendaEvents_infrastructure

router = APIRouter()

@router.post("/addEvent/")
def addEvent(event: calendarEventsModel.Event):
    return calendaEvents_infrastructure.add_event(event)