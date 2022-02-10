from django.urls import path
from . import views
"""urlpatterns = [
    path('', views.index),	   
]"""

from django.conf import settings

if settings.DEBUG:
    urlpatterns = [
        path('', views.debug),
    ]