import urllib2
from urllib import urlencode
f = open('cities.txt')

for line in f:
    (city, lon, lat) = line.split("\t")

    url = 'http://timezone-lookup.com/' 
    args = {'coords': "%s,%s" % (lon, lat)}
    full_url = '%s?%s' % (url, urlencode(args))
    try:
        response = urllib2.urlopen(full_url)
        print response.read()
    except:
        print "Couldn't find %s" % city
