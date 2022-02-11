from django.urls import path, include
from django.contrib import admin

from . import views


urlpatterns = [
    path('', include('login.urls')),
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('profile/home', views.home),
]
