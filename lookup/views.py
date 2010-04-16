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


def browse(request, country=None):  

    timezones = []
    for zone in  Zone.objects.values_list('tzid').order_by('tzid').distinct():
        timezones.append(str(zone[0]))

    return render_to_response('browse.html', {
            'timezones': timezones
    
            })


def map( request, timezone):  
  #  all_tz = Zone.objects.all()
    gz = GoogleZoom()
    all_tz = Zone.objects.filter(tzid=timezone)
    centoid = all_tz.unionagg().centroid
    return render_to_response('map.html', {
            'all_tz': all_tz,
            'zoom': gz.get_zoom(all_tz.unionagg())

            })
