from calendarCourt1.models.calendarEventsModel import Event
from google.oauth2 import service_account
from googleapiclient.discovery import build
from models import response
from fastapi import HTTPException
from dotenv import load_dotenv
import os

load_dotenv()

# Leer las variables de entorno
SERVICE_ACCOUNT_INFO = {
    "type": os.getenv("TYPE_COURT1"),
    "project_id": os.getenv("PROJECT_ID_COURT1"),
    "private_key_id": os.getenv("PRIVATE_KEY_ID_COURT1"),
    "private_key": os.getenv("PRIVATE_KEY_COURT1").replace('\\n', '\n'),  # Reemplazar \n por saltos de línea
    "client_email": os.getenv("CLIENT_EMAIL_COURT1"),
    "client_id": os.getenv("CLIENT_ID_COURT1"),
    "auth_uri": os.getenv("AUTH_URI_COURT1"),
    "token_uri": os.getenv("TOKEN_URI_COURT1"),
    "auth_provider_x509_cert_url": os.getenv("AUTH_PROVIDER_X509_CERT_URL_COURT1"),
    "client_x509_cert_url": os.getenv("CLIENT_X509_CERT_URL_COURT1"),
    "universe_domain": os.getenv("UNIVERSE_DOMAIN_COURT1")
}

# Definir los alcances de la API de Google Calendar
SCOPES = ['https://www.googleapis.com/auth/calendar']

# Cargar credenciales de la cuenta de servicio desde el diccionario
credentials = service_account.Credentials.from_service_account_info(
    SERVICE_ACCOUNT_INFO,
    scopes=SCOPES
)

# Construir el servicio de Google Calendar
service = build('calendar', 'v3', credentials=credentials)

def add_event_court1(event: Event):
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
        created_event = service.events().insert(calendarId='beachpointdev@gmail.com', body=event_body).execute()
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
