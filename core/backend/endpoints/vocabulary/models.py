from django.db import models


class Word(models.Model):
    """Class Word."""

    german_translation = models.CharField(max_length=255)
    english_translation = models.CharField(max_length=255)
    french_translation = models.CharField(max_length=255, null=True, blank=True)
    approved = models.BooleanField(default=False)

    objects = models.Manager()
