from dotenv import load_dotenv
import smtplib, ssl
import os


def email_send(message):
    host = "smtp.gmail.com"
    port = 465

    load_dotenv()
    app_password = os.getenv("GMAIL_PASSWORD")

    user_name = "elaradomingos@gmail.com"
    password = app_password
    receiver = "elaradomingos@gmail.com"

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(user_name, password)
        server.sendmail(user_name, receiver, message)
