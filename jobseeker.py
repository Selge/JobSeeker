import smtplib
from email.mime.text import MIMEText
from email.header import Header

import messages, settings


def send_email(message):
    # sender = "your.email@isegal.de"
    # password = "##whatever**"

    # server = smtplib.SMTP("smtp.gmail.com", 587)
    sender = settings.get_settings()[0]
    password = settings.get_settings()[1]
    server = settings.get_settings()[2]

    server.starttls()

    try:
        server.login(sender, password)
        mime = MIMEText(message, 'plain', 'utf-8')
        server.sendmail(sender, sender, mime.as_string())

        return "The message was sent successfully!"

    except Exception as _ex:
        return f"{_ex}\nSomething went wrong... Please, check your settings!"


def main():
    message = input("Type in your message here:  ")
    print(send_email(message=message))


if __name__ == '__main__':
    main()
