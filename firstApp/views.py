from django.shortcuts import render
from django.http import HttpResponse
import datetime

def display(request):
    return HttpResponse("<h1>Hola Mundo!</h1>")

def displayDateTime(request):
    dt=datetime.now()
    s="<b>La hora es: "+str(dt)+"</b>"
    return HttpResponse(s)

# Create your views here.
