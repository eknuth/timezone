from django.conf.urls.defaults import *
from lookup import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^timezone/', include('timezone.foo.urls')),
                       (r'^map/(?P<country>.*)$', views.map),
                       (r'^map$', views.map),
                       (r'^search$', views.search),
                       (r'^browse$', views.browse),
                       

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
