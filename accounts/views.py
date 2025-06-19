from django.contrib.auth import logout
from django.shortcuts import render, redirect


# Create your views here.
def user_logout(request):
    logout(request)
    return redirect(request.META.get('HTTP_REFERER', '/')) #Zůstanu na stejné stránce