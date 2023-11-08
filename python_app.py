from dotenv import load_dotenv
import os
from email.message import EmailMessage
import ssl
import smtplib

load_dotenv()
password = os.getenv("PASS")
sender = os.getenv("SENDER")
resiver = os.getenv("RESIVER")

email_sender = sender
email_password = password

email_resiver = resiver

subject = "Test02 poruka"

body = """
Ovo je presonalna skripta koja šalje mejlove koristeći Python. 
Hvala Vam na razumevanju

Bratislav Nikolić
""" 

em = EmailMessage()

em["From"] = email_sender
em["To"] = email_resiver
em["Subject"] = subject
em.set_content(body)

contex = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com",465, context = contex) as smtp:
    smtp.login (email_sender, email_password)
    smtp.sendmail(email_sender, email_resiver, em.as_string())
