import requests

from rest_framework import viewsets
from rest_framework.response import Response
from django.conf import settings

from django.core.mail import send_mail


class SendMailViewSet(viewsets.ViewSet):
    def create(self, request):
        data = request.data

        req = requests.post(
            "https://api.mailgun.net/v3/sandbox65ed4e1ca75d4737bdc36a5ee14bd859.mailgun.org/messages",
            auth=("api", settings.API_KEY_MAILGUN),
            data={
                "from": "Mailgun Sandbox <postmaster@sandbox26424d591b39449a853bbe56906d5605.mailgun.org>",
                "to": "sadour.mehdi@gmail.com",
                "subject": f'{data.get("name")} want to contact you',
                "text": data.get("message"),
            },
        )
        # send_mail(
        #     subject=f'{data.get("name")} want to contact you',
        #     message=data.get("message"),
        #     from_email=data.get("from_email"),
        #     recipient_list=['sadour.mehdi@gmail.com'],
        #     fail_silently=False,
        # )
        return Response(status=201)
