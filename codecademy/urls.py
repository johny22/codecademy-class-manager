from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('parser2.urls'))
]