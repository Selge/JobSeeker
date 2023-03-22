import smtplib
from email.mime.text import MIMEText
from email.header import Header

import messages
import settings


def send_email(message):
    sender = settings.get_sender()
    password = settings.get_key()
    server = smtplib.SMTP("smtp.gmail.com", 587)

    server.starttls()

    try:
        server.login(sender, password)
        mime = MIMEText(message, 'plain', 'utf-8')
        message["Subject"] = messages.get_subject()
        server.sendmail(sender, sender, mime.as_string())

        return "The message was sent successfully!"

    except Exception as _ex:
        return f"{_ex}\nSomething went wrong... Please, check your settings!"


def main():
    message = messages.get_message()
    print(send_email(message=message))


if __name__ == '__main__':
    main()
