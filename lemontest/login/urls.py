from django.urls import path
from django.conf import settings

from . import views


if settings.DEBUG:
    urlpatterns = [
        path('', views.debug),
    ]
