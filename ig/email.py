from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_welcome_email(name,receiver):

    # Creating message subject and sender
    subject = 'Welcome to the Instagram'
    sender = 'elvisbkt@gmail.com'

    #passing in the context vairables
    text_content = render_to_string('email/instaemail.txt',{"name": name})
    html_content = render_to_string('email/instaemail.html',{"name": name})

    