from django.db import models


class Location(models.Model):
    
    city = models.CharField(max_length=50, editable=True, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)