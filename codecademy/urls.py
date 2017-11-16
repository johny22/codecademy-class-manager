from django.conf.urls import include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from codecademy.parser2.views import *
admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'codecademy.views.home', name='home'),
    # url(r'^codecademy/', include('codecademy.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
   url(r'^addDB/$', InserirNoBD),
   url(r'^charts/(?P<PK>\d+)/$', charts),
   url(r'^badges/(?P<PK>\d+)/$', badges),
   url(r'^track_percent/(?P<PK>\d+)/$', track_percent),
   url(r'^admin/', include(admin.site.urls)),
   url(r'^$', index, name='home'),
   url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': '/home/jones/codecademy/codecademy/static/'}),
]