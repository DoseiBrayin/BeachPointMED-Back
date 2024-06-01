from calendarCourt2.models.calendarEventsModel import Event
import os
from google.oauth2 import service_account
from googleapiclient.discovery import build 
from fastapi import HTTPException
from models import response

SERVICE_ACCOUNT_INFO = {
    "type": os.getenv("TYPE_COURT2"),
    "project_id": os.getenv("PROJECT_ID_COURT2"),
    "private_key_id": os.getenv("PRIVATE_KEY_ID_COURT2"),
    "private_key": os.getenv("PRIVATE_KEY_COURT2").replace('\\n', '\n'),  # Reemplazar \n por saltos de línea
    "client_email": os.getenv("CLIENT_EMAIL_COURT2"),
    "client_id": os.getenv("CLIENT_ID_COURT2"),
    "auth_uri": os.getenv("AUTH_URI_COURT2"),
    "token_uri": os.getenv("TOKEN_URI_COURT2"),
    "auth_provider_x509_cert_url": os.getenv("AUTH_PROVIDER_X509_CERT_URL_COURT2"),
    "client_x509_cert_url": os.getenv("CLIENT_X509_CERT_URL_COURT2"),
    "universe_domain": os.getenv("UNIVERSE_DOMAIN_COURT2")
}

SCOPES = ['https://www.googleapis.com/auth/calendar']

credentials = service_account.Credentials.from_service_account_info(
    SERVICE_ACCOUNT_INFO,
    scopes=SCOPES
)

service = build('calendar', 'v3', credentials=credentials)

def add_event_court2(event: Event):
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
        created_event = service.events().insert(calendarId='beachpointdev2@gmail.com', body=event_body).execute()
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