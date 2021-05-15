from django.contrib.gis import admin

from .models import Marker

@admin.register(Marker)
class MarkerAdmin(admin.OSMGeoAdmin):

    list_display = ("name", "location")

