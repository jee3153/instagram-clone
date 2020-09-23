from django.db import models
from django.utils.timezone import now
from . import managers


class TimeStampedModel(models.Model):

    """ Time Stamped Model """

    created = models.DateTimeField(default=now)
    updated = models.DateTimeField(default=now)
    objects = managers.CustomModelManager()

    class Meta:
        abstract = True
