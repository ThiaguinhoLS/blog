# -*- coding: utf-8 -*-

from app import mail
from flask_mail import Message

def send_email(subject, sender, recipients, text_body, html_body):
    message = Message(
        subject=subject,
        sender=sender,
        recipients=recipients,
        body=text_body,
        html=html_body
    )
    mail.send(message)
