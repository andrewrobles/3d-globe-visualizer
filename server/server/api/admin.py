from django.contrib import admin
from .models import Marker

@admin.register(Marker)
class MarkerAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'latitude', 'longitude', 'altitude')
