from django.db import models


class Verb(models.Model):
    """Class Verb."""

    verb_in_present = models.CharField(max_length=255)
    english_translation = models.CharField(max_length=255)
    french_translation = models.CharField(max_length=255, null=True, blank=True)
    past_participle = models.CharField(max_length=255, null=True, blank=True)
    simple_past = models.CharField(max_length=255, null=True, blank=True)
    approved = models.BooleanField(default=False)

    objects = models.Manager()
