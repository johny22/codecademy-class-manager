from django.urls import include, path
from django.contrib import admin

from .views import *

admin.autodiscover()

urlpatterns = [
   path('addDB/', InserirNoBD),
   path('charts/<int:pk>/', charts),
   path('badges/<int:pk>/', badges),
   path('track_percent/<int:pk>/', track_percent),
   path('', index, name='home')
]