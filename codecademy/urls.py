from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'codecademy.views.home', name='home'),
    # url(r'^codecademy/', include('codecademy.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
   url(r'^addDB/$', 'codecademy.parser2.views.InserirNoBD'),
   url(r'^charts/(?P<PK>\d+)/$', 'codecademy.parser2.views.charts'),
   url(r'^badges/(?P<PK>\d+)/$', 'codecademy.parser2.views.badges'),
   url(r'^track_percent/(?P<PK>\d+)/$', 'codecademy.parser2.views.track_percent'),
   url(r'^admin/', include(admin.site.urls)),
   url(r'^$', 'codecademy.parser2.views.index', name='home'),
   url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': '/home/jones/codecademy/codecademy/static/'}),
)
