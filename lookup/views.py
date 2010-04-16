from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

from django.contrib.gis.geos import Point
from django.contrib.gis.maps.google import GoogleZoom

import pytz
import simplejson
import datetime

from models import Zone
from forms import SearchForm



def get_timezone_by_point(point):
    """
    Get Timezone by Point
    """
    return Zone.objects.get(geom__intersects=point)


def search(request):
    if request.GET.get('coords', ''):
        form = SearchForm(request.GET)
        if form.is_valid():
            (lat,lon) = form.cleaned_data['coords'].split(',')
            n = get_timezone_by_point(Point(float(lat),float(lon)))
            tz = pytz.timezone(n.tzid)
            time = tz.localize(datetime.datetime.now())
            fmt = '%Y-%m-%d %H:%M:%S %Z%z'
            offset_fmt = '%z'
            abbr_fmt = '%Z'
            search_response = {'name': n.tzid, #'time': time.strftime(fmt), 
                               'offset': time.strftime(offset_fmt),
                               'abbr': time.strftime(abbr_fmt) }
            return HttpResponse(simplejson.dumps(search_response),
                                    mimetype='application/json')

    else:
        form = SearchForm()
       
        return render_to_response('search.html', {
                'form': form,
                })


def browse(request):  
    all_tzid = Zone.objects.values_list('tzid').order_by('tzid').distinct()
    
    return render_to_response('browse.html', {
            'all_tzid': all_tzid
            })

def map(request):  
    all_tz = Zone.objects.all()
    gz = GoogleZoom()
    print "starting to render"
    return render_to_response('map.html', {
            'centroid': all_tz.unionagg().centroid, 
            'zoom_level': 0,
            })
