import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
from utils.logger import setup_logger

log = setup_logger()

load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

def send_mail(to,subject,body):
    if not EMAIL_ADDRESS or not EMAIL_PASSWORD:
        log.error("Invalid email or password")
        return False
    
    try:
        message = MIMEMultipart()
        message["From"] = EMAIL_ADDRESS
        message["To"] = to
        message["Subject"] = subject
        message.attach(MIMEText(body,"plain"))
        
        with smtplib.SMTP_SSL("smtp.gmail.com",465) as server:
            server.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
            server.send_message(message)
        log.info(f"Email Sent Successfully -> {to}")
        return True
    except smtplib.SMTPAuthenticationError:
        log.error("Login Error")
        return False
    except Exception as e:
        log.error(f"Email sending error {e}")
        return False