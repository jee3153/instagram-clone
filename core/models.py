from django.db import models
from django.utils.timezone import now


class TimeStampedModel(models.Model):

    """ Time Stamped Model """

    created = models.DateTimeField(default=now)
    updated = models.DateTimeField(default=now)

    class Meta:
        abstract = True
