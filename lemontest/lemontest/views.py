from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponse


@login_required
def home(request):
    if request.user.is_superuser:
        return HttpResponse("Welcome " + request.user.username + " you're an administrator")
    else:
        return HttpResponse("Welcome " + request.user.username + " you're an user")
