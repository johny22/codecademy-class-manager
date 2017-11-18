from django.conf.urls import include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from codecademy.parser2.views import *
admin.autodiscover()

urlpatterns = [
   url(r'^addDB/$', InserirNoBD),
   url(r'^charts/(?P<PK>\d+)/$', charts),
   url(r'^badges/(?P<PK>\d+)/$', badges),
   url(r'^track_percent/(?P<PK>\d+)/$', track_percent),
   url(r'^admin/', include(admin.site.urls)),
   url(r'^$', index, name='home')
]