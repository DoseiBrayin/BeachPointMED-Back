from fastapi import APIRouter
from calendarCourt1.models import calendarEventsModel
from calendarCourt1.infrastructure import calendarEvents_infrastructure

router = APIRouter()

@router.post("/addEvent_Court1/")
def addEvent(event: calendarEventsModel.Event):
    return calendarEvents_infrastructure.add_event_court1(event)