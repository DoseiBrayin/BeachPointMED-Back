from calendarEvents.models.calendarEventsModel import Event

def add_event(event: Event):
    event_body = {
        'summary': event.summary,
        'start': {
            'dateTime': event.start,
            'timeZone': event.time_zone
        },
        'end': {
            'dateTime': event.end,
            'timeZone': event.time_zone
        }
    }

    #try: 
    #    created_event = 