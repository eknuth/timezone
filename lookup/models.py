# This is an auto-generated Django model module created by ogrinspect.
from django.contrib.gis.db import models

class Zone(models.Model):
    tzid = models.CharField(max_length=30)
    geom = models.MultiPolygonField()
    objects = models.GeoManager()

# Auto-generated `LayerMapping` dictionary for Zone model
zone_mapping = {
    'tzid' : 'TZID',
    'geom' : 'MULTIPOLYGON',
}
