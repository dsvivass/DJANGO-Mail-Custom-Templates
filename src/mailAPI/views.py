from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from decouple import config
import json
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

# Create your views here.


def send_email(request):
    # email = EmailMessage(
    #     'Title',
    #     'Body message',
    #     config('EMAIL_HOST_USER'),
    #     [config('TO_EMAIL')],
    # )
    # # email.attach('DLNet_Nimbus.txt', txtFile.read(), txtFile.content_type)
    # email.send()

    emailSubject = "Subject"
    emailOfSender = config('EMAIL_HOST_USER')
    emailOfRecipient = config('TO_EMAIL')

    # Note I used a normal tuple instead of  Context({"username": "Gilbert"}) because Context is deprecated. When I used Context, I got an error > TypeError: context must be a dict rather than Context
    context = ({"name": "Gilbert"})

    text_content = render_to_string('mail.txt', context, request=request)
    html_content = render_to_string('mail.html', context, request=request)

    try:
    # I used EmailMultiAlternatives because I wanted to send both text and html
        emailMessage = EmailMultiAlternatives(subject=emailSubject, body=text_content, from_email=emailOfSender, to=[
                                            emailOfRecipient, ], reply_to=[emailOfSender, ])
        emailMessage.attach_alternative(html_content, "text/html")
        emailMessage.send(fail_silently=False)

    except SMTPException as e:
        print('There was an error sending an email: ', e)
        error = {'message': ",".join(e.args) if len(e.args) > 0 else 'Unknown Error'}
        raise serializers.ValidationError(error)


class sendEmailAPIView(APIView):

    def post(self, request, format=None):

        send_email(request)

        return Response(status=status.HTTP_200_OK)
