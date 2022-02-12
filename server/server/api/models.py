from django.db import models

class Marker(models.Model):
    latitude = models.DecimalField(max_digits=9, decimal_places=5)
    longitude = models.DecimalField(max_digits=9, decimal_places=5)
    altitude = models.DecimalField(max_digits=9, decimal_places=5)

    def __str__(self):
        return 'Marker object ({})'.format(self.id)