from django.conf import settings
from django.core.mail import send_mail

# f4rmx1@gmail.com & t..!
# client_bca@outlook.com

def email_requested(instance):
    subject = "Request Has Been Made"
    message = "A connection request has been made: \n" + str(instance.user) + " " + str(instance.direction) + " " + str(instance.client) + " of message type " + str(instance.message_type)
    from_email = settings.EMAIL_HOST_USER
    to_list = [str(instance.client)]
    send_mail(subject, message, from_email, to_list, fail_silently=True)


def email_modified(data):
    subject = "Request Has Been Modified"
    message = "A connection request has been modified: \n" + str(data.user) + " " + str(data.direction) + " " + str(data.client) + " of message type " + str(data.message_type)
    from_email = settings.EMAIL_HOST_USER
    to_list = [str(data.client)]
    send_mail(subject, message, from_email, to_list, fail_silently=True)


def email_request_response(data):
    subject = "Request Has Been " + str(data.status)
    message = "Connection request has been " + str(data.status) + ": \n" + str(data.user) + " " + str(data.direction) + " " + str(data.client) + " of message type " + str(data.message_type)
    from_email = settings.EMAIL_HOST_USER
    to_list = [str(data.user)]
    send_mail(subject, message, from_email, to_list, fail_silently=True)