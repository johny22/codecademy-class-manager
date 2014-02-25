from django.conf.urls.defaults import patterns, include, url
from codecademy.views import InserirNoDB

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
   url(r'^view1/$', InserirNoDB),
   url(r'^admin/', include(admin.site.urls)),
)
