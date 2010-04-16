# This is an auto-generated Django model module created by ogrinspect.
from django.contrib.gis.db import models
from django.contrib.gis.maps.google.overlays import GPolygon

class Zone(models.Model):
    tzid = models.CharField(max_length=30)
    geom = models.MultiPolygonField()
    objects = models.GeoManager()

    def gpoly(self):
        gpoly = GPolygon(self.poly)
        return gpoly.points.replace('GLatLng', 'google.maps.LatLng')


# Auto-generated `LayerMapping` dictionary for Zone model
zone_mapping = {
    'tzid' : 'TZID',
    'geom' : 'MULTIPOLYGON',
}
