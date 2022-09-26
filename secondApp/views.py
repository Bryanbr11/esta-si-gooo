import datetime
from django.shortcuts import render
from django.http import HttpResponse

def display(request):
    return HttpResponse("<h1>Ejemplo app2 2 vista 1</h1>")

def displayDateTime(request):
    dt=datetime.now()
    s="<b>La hora es: "+str(dt)+"</b>"
    return HttpResponse(s)

# Create your views here.
