from calendarEvents.models.calendarEventsModel import Event
from google.oauth2 import service_account
from googleapiclient.discovery import build
from models import response
from fastapi import HTTPException

# Ruta al archivo JSON de credenciales de la cuenta de servicio
SERVICE_ACCOUNT_FILE = 'path/to/your/service-account-file.json'

# Definir los alcances de la API de Google Calendar
SCOPES = ['https://www.googleapis.com/auth/calendar']

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE,
    scopes=SCOPES
)

service = build('calendar', 'v3', credentials=credentials)

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

    try: 
       created_event = service.events().insert(calendarId='primary', body=event_body).execute()
       return response.APIResponse(
           message="Event created successfully",
           data=created_event.get('htmlLink'),
           status="success",
           status_code=200
       ).__dict__
    except Exception as e:
        raise HTTPException(status_code=500, detail=response.APIResponse(
            message="An error occurred while creating the event",
            data=str(e),
            status="error",
            status_code=500
        ).__dict__)