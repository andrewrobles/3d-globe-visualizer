from django.db import models

class Marker(models.Model):
    latitude = models.DecimalField(max_digits=8, decimal_places=5)
    longitude = models.DecimalField(max_digits=8, decimal_places=5)
    altitude = models.DecimalField(max_digits=8, decimal_places=5)