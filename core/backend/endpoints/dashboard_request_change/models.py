from datetime import datetime

from django.db import models
from jsonfield import JSONField

from core.backend.endpoints.verb.models import Verb
from core.backend.endpoints.vocabulary.models import Word


class StatusChoice(models.TextChoices):
    """Class StatusChoice."""

    PENDING = "Pending"
    ACCEPTED = "Accepted"
    REJECTED = "Rejected"


class VerbRequest(models.Model):
    """Class WordRequestChange"""

    item = models.ForeignKey(Verb, on_delete=models.CASCADE)
    data = JSONField(default={})
    status = models.CharField(max_length=255, default="Pending", choices=StatusChoice.choices)
    message = models.CharField(max_length=255, default="Change request is in review.", blank=True)
    date = models.DateTimeField(default=datetime.now)

    objects = models.Manager()


class WordRequest(models.Model):
    """Class WordRequestChange"""

    item = models.ForeignKey(Word, on_delete=models.CASCADE)
    data = JSONField(default={})
    status = models.CharField(max_length=255, default="Pending", choices=StatusChoice.choices)
    message = models.CharField(max_length=255, default="Change request is in review.", blank=True)
    date = models.DateTimeField(default=datetime.now)

    objects = models.Manager()
