import os
from django.contrib.gis.utils import LayerMapping
from models import Zone, zone_mapping


zone_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/world/tz_world.shp'))

def run(verbose=True):
    lm = LayerMapping(Zone, zone_shp, zone_mapping,
                      transform=False, encoding='iso-8859-1')

    lm.save(strict=True, verbose=verbose)
