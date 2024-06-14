from fastapi import HTTPException, APIRouter
from fastapi_mail import MessageSchema, FastMail, ConnectionConfig
import os

conf = ConnectionConfig(
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME"),
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD"),
    MAIL_FROM = os.environ.get("MAIL_USERNAME"),
    MAIL_PORT = 587,
    MAIL_SERVER = "smtp.gmail.com",
    MAIL_FROM_NAME="BeachPoint",
    MAIL_STARTTLS = True,
    MAIL_SSL_TLS = False,
    USE_CREDENTIALS = True,
    VALIDATE_CERTS = False
)

async def sendEmail(email, body, subject):
    try :
        message = MessageSchema(
        subject=subject,
        recipients=email,
        body=body,
        subtype="html",
        )

        fm = FastMail(conf)
        await fm.send_message(message)
        return message
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error sending email: {str(e)}")

# 
# message = {
#         "email": ["example@gmail.com"],
#         "subject": "Hello from FastAPI",
#         "body": "<h1>This is a test email</h1><p>Sent with FastAPI and fastapi-mail</p>"
#     }
