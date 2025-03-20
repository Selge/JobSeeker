def get_message():
    with open('email/standard/message_text.txt', 'r', encoding='utf-8') as message_text:
        message = message_text.read()
    return message


def get_subject():
    with open('email/standard/message_subject.txt', 'r', encoding='utf-8') as letter_subject:
        subject = letter_subject.read()
    return subject


def get_receiver():
    with open('email/standard/receivers.txt', 'r', encoding='utf-8') as receivers:
        receiver = receivers.read().splitlines()
    return receiver
