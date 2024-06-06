from pydantic import BaseModel
from google.oauth2 import service_account
from googleapiclient.discovery import build
from fastapi import HTTPException
from datetime import datetime
import os


class Event(BaseModel):
    summary: str
    start: str
    end: str
    time_zone: str
    court: str


# {
#   "summary": "Meeting with team",
#   "start": "2024-06-06T10:00:00-05:00",
#   "end": "2024-06-06T11:00:00-05:00",
#   "time_zone": "America/Chicago",
#   "court": "court medellin-1" || "court medellin-2"
# }


# Define the scopes for the Google Calendar API
SCOPES = ['https://www.googleapis.com/auth/calendar']

def create_events_calendar(event: Event):
    try:
        datetime.fromisoformat(event.start)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid start date format. It should be in ISO 8601 format")
    
    try:
        datetime.fromisoformat(event.end)   
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid end date format. It should be in ISO 8601 format")
    
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


    # Local variables
    SERVICE_ACCOUNT_INFO = {}
    COURT_EMAIL = ''

    if '1' in event.court:
        COURT_EMAIL = 'beachpointdev@gmail.com'
        SERVICE_ACCOUNT_INFO = {
            "type": os.getenv("TYPE_COURT1"),
            "project_id": os.getenv("PROJECT_ID_COURT1"),
            "private_key_id": os.getenv("PRIVATE_KEY_ID_COURT1"),
            "private_key": os.getenv("PRIVATE_KEY_COURT1").replace('\\n', '\n'),  # Replace \n with line breaks
            "client_email": os.getenv("CLIENT_EMAIL_COURT1"),
            "client_id": os.getenv("CLIENT_ID_COURT1"),
            "auth_uri": os.getenv("AUTH_URI_COURT1"),
            "token_uri": os.getenv("TOKEN_URI_COURT1"),
            "auth_provider_x509_cert_url": os.getenv("AUTH_PROVIDER_X509_CERT_URL_COURT1"),
            "client_x509_cert_url": os.getenv("CLIENT_X509_CERT_URL_COURT1"),
            "universe_domain": os.getenv("UNIVERSE_DOMAIN_COURT1")
        }
    elif '2' in event.court:
        COURT_EMAIL = 'beachpointdev2@gmail.com'
        SERVICE_ACCOUNT_INFO = {
            "type": os.getenv("TYPE_COURT2"),
            "project_id": os.getenv("PROJECT_ID_COURT2"),
            "private_key_id": os.getenv("PRIVATE_KEY_ID_COURT2"),
            "private_key": os.getenv("PRIVATE_KEY_COURT2").replace('\\n', '\n'),  # Replace \n with line breaks
            "client_email": os.getenv("CLIENT_EMAIL_COURT2"),
            "client_id": os.getenv("CLIENT_ID_COURT2"),
            "auth_uri": os.getenv("AUTH_URI_COURT2"),
            "token_uri": os.getenv("TOKEN_URI_COURT2"),
            "auth_provider_x509_cert_url": os.getenv("AUTH_PROVIDER_X509_CERT_URL_COURT2"),
            "client_x509_cert_url": os.getenv("CLIENT_X509_CERT_URL_COURT2"),
            "universe_domain": os.getenv("UNIVERSE_DOMAIN_COURT2")
        }
    
    if not COURT_EMAIL or not SERVICE_ACCOUNT_INFO:
        raise HTTPException(status_code=400, detail="Service account information or court email not specified correctly")

    CREDENTIALS = service_account.Credentials.from_service_account_info(
        SERVICE_ACCOUNT_INFO,
        scopes=SCOPES
    )
    service = build('calendar', 'v3', credentials=CREDENTIALS)
    
    try:
        created_event = service.events().insert(calendarId=COURT_EMAIL, body=event_body).execute()
        return created_event.get('htmlLink')
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating the event: {str(e)}")
