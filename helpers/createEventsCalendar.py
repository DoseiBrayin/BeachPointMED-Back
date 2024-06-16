import json
from google.oauth2 import service_account
from googleapiclient.discovery import build
from fastapi import HTTPException
from datetime import datetime
import os
from dotenv import load_dotenv

# {
#   "summary": "Meeting with team",
#   "start": "2024-06-06T10:00:00-05:00",
#   "end": "2024-06-06T11:00:00-05:00",
#   "time_zone": "America/Chicago",
#   "court": "court medellin-1" || "court medellin-2"
# }


# Define the scopes for the Google Calendar API
SCOPES = ['https://www.googleapis.com/auth/calendar']

def create_events_calendar(event):
    try:
        datetime.fromisoformat(event["start"])
    except ValueError:
        print("Error start")
        raise HTTPException(status_code=400, detail="Invalid start date format. It should be in ISO 8601 format")
    
    try:
        datetime.fromisoformat(event["end"])   
    except ValueError:
        print("Error end")
        raise HTTPException(status_code=400, detail="Invalid end date format. It should be in ISO 8601 format")
    
    event_body = {
        'summary': event["summary"],
        'start': {
            'dateTime': event["start"],
            'timeZone': event["time_zone"]
        },
        'end': {
            'dateTime': event["end"],
            'timeZone': event["time_zone"]
        }
    }

    SERVICE_ACCOUNT_INFO = {}
    COURT_EMAIL = ''

    if '1' in event["court"]:
        SERVICE_ACCOUNT_INFO = {
            "type": os.getenv("TYPE_COURT1"),
            "project_id": os.getenv("PROJECT_ID_COURT1"),
            "private_key_id": os.getenv("PRIVATE_KEY_ID_COURT1"),
            "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQD4Uv8kcy0BGz78\nwrzyIEGd4I38QAksfHcL7Ik4QDwp+G+g3L+2H7K6Ejwgsp3c+srFBM3nxx/gvqgY\nLHbcDDCHzyyrvP1Os27p6KAWeMZ8ViuXl0qG8yJjXXs/QcGxciV3ehtAQMLUDUfH\nVp/s7Y5jMcZhvPmBq5T973AR9F4HgoBRJDlvXb3pqhMQv2tbrp9xoHdyL7MaJ8Oq\n2Lg272GkLRDpdS4bev0By6v3gXg72QztqDfpUMSDnLbCV7sEhUUNLec0BfgOZkTA\nqlW3KVL818/0scnlVqC1DzZ9rB+i7rTNgILkkJ6jGgfgIzZk+b6lBa7MpmQiU4ZQ\nldvZ+9ZXAgMBAAECggEAAIjFLcHlrePuHcMZfvfczEcoZwuIOYVHCEqI/Qr+ViTH\nsLPo4a5txwK1CGj59/i+KPBatQ3znpsqZ2rpEo4gKJqkgPYWIW43Zd9vQL0fyDKz\nQ087BNFPGKGh2z/797LEK96iYmABS02AAwjHrU3RiZsYzysF6maBGo7CUfeRoDiB\nkmz73lofZ2GAN3gQY0mw7t1BsxWdM5bu4gURxKhFM1dOZsONgoniBL4MqlLVwkr0\nZYGCqxjSzSi3Rf2bIvlTjlr55sefyrIvB7iB4YoNmnGui9B0vxyiBy3z6RwslNWs\n9SF3iG+sPB7DqEmHefk/2Ph1pM7Ij8XwDqxpUQ17+QKBgQD9OIc/n80n+rnOTr4K\nc20ezCEKsIJfdRAmykIAe/p/dMdFv6NmhPQrSj2/JjoGA1OA5Ez+3jLs+uaLjFfJ\nLpBLbOcdWOMhjUIWea/VbMIUZbB2SIzL9ulWfvtmcWCFmc7zL6gNjkosPLfTdon2\npolTPhqjaY1M0xqE9SQh18hvswKBgQD7DLXcJrrJq+8vBn0Zdbq/LyOe+WQu9ozE\n5/ARMOad5dp1s+NwRe1MCvLbzL1PfgjVo9n/qC5d66FpeWVjKnMa4nzKTJCNTIiJ\nOxvnsgMgo1hjqlMt6+wgyv3cpKbxKydlX1gpQe4UXU6jEhxmxjMDg2kFdHp2hpmK\nO7peYsoMzQKBgQD0sYVwpBl6Ar0+cbUPIE9YLWXYkIzLdbHv6g8xrJx6Qfy2l+Ns\nlBnnI0zbxDLZ0KkGqpcEyu9nNWVHgIzsKgTh/hCvuU9zAq/UTC7wDLLXRxTomF8G\nUklVfkutyO2+7MyhD3JT9yYR7XKt86SKJpAZUrAnLT6P+Idt5/3MflqAJQKBgQC8\nCBMWJzPz5QEqmZONRC5xD5+AbI5q1mMtAANA/P1d+lCbo/aPmvBW6kRn+Hs6VM3N\nJgIbiB3iXp/w3engUmUQF98brij+i/ofvtPxv9Sz12RWkbXnSTL8hM2LOw+Gxqml\nNbpUfHsTaaeCYAhBueVvljdMzKcEq1/It1+pXhizaQKBgQDeISW+BrkgiQDG9Lkh\nU1vTSQ/nRbMd9IqFYjSh+N/p8AvQR7Kk3ISiqZVnzSnqgX14ho6yPNk6g2YW9+JB\nTB3X7rZcZG9ZLb1TxQ/yX4wufEq17/DlX7NOQTizlWN2ibeCwCcZnh8MlYqpFPmU\nm8gjNTEz0FC+6db52qxnPfQVPA==\n-----END PRIVATE KEY-----",
            "client_email": os.getenv("CLIENT_EMAIL_COURT1"),
            "client_id": os.getenv("CLIENT_ID_COURT1"),
            "auth_uri": os.getenv("AUTH_URI_COURT1"),
            "token_uri": os.getenv("TOKEN_URI_COURT1"),
            "auth_provider_x509_cert_url": os.getenv("AUTH_PROVIDER_X509_CERT_URL_COURT1"),
            "client_x509_cert_url": os.getenv("CLIENT_X509_CERT_URL_COURT1"),
            "universe_domain": os.getenv("UNIVERSE_DOMAIN_COURT1")
        }
        COURT_EMAIL = 'beachpointdev@gmail.com'
    elif '2' in event["court"]:
        SERVICE_ACCOUNT_INFO = {
            'type': os.getenv('TYPE_COURT2'),
            'project_id': os.getenv('PROJECT_ID_COURT2'),
            'private_key_id': os.getenv('PRIVATE_KEY_ID_COURT2'),
            'private_key': os.getenv('PRIVATE_KEY_COURT2').replace('\\n', '\n'),
            'client_email': os.getenv('CLIENT_EMAIL_COURT2'),
            'client_id': os.getenv('CLIENT_ID_COURT2'),
            'auth_uri': os.getenv('AUTH_URI_COURT2'),
            'token_uri': os.getenv('TOKEN_URI_COURT2'),
            'auth_provider_x509_cert_url': os.getenv('AUTH_PROVIDER_X509_CERT_URL_COURT2'),
            'client_x509_cert_url': os.getenv('CLIENT_X509_CERT_URL_COURT2'),
            'universe_domain': os.getenv('UNIVERSE_DOMAIN_COURT2')
        }
        COURT_EMAIL = 'beachpointdev2@gmail.com'

    # print(type(SERVICE_ACCOUNT_INFO))
    # private_key = os.getenv("PRIVATE_KEY_COURT1").replace('\\n', '\n')
    # print(private_key.startswith('-----BEGIN PRIVATE KEY-----'))
    # print(private_key.endswith('-----END PRIVATE KEY-----'))

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
