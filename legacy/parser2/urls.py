from django.urls import include, path
from django.contrib import admin

from .views import *

admin.autodiscover()

urlpatterns = [
   path('addDB/', InserirNoBD),
   path('charts/<int:perfil_id>/', charts),
   path('badges/<int:perfil_id>/', badges),
   path('track_percent/<int:perfil_id>/', track_percent),
   path('', index, name='home')
]