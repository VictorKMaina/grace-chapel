import os
from sendgrid import SendGridAPIClient
from django.conf import settings
from sendgrid.helpers.mail import Mail
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site


def send_visitor_welcome(request, visitor):
    message = Mail(
        from_email="moringacoreprojects@gmail.com",
        to_emails=visitor.email,
        subject="Introduction",
        html_content=render_to_string('email/welcome_visitor.html', {
            'visitor': visitor,
        }))

    try:
        sg = SendGridAPIClient(api_key=settings.SENDGRID_API_KEY)
        response = sg.send(message)
        print("SENDGRID RESPONSE CODE: ", response.status_code)
    except Exception as e:
        print("\nSENDGRID ERROR: ", e, "\n")
