from fastapi import APIRouter
from calendarCourt2.models import calendarEventsModel
from calendarCourt2.infrastructure import calendarEvents_infrastructure


router = APIRouter()


@router.post("/addEvent_Court2/")
def addEvent(event: calendarEventsModel.Event):
    return calendarEvents_infrastructure.add_event_court2(event)