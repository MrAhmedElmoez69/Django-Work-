from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.


def homePage(request):
    return render('<h1> Title here </h1> ')


def homePage1(request):
    return render(
        request,
        'events/homePage.html'
        )


def listEventsStatic(request):
    list = [
      {
        'title': 'Arto Hellas',
        'description': 1
      },
      {
        'tilte': 'Ada Bella',
        'description': 2
      },
       {
        'tilte': 'Leon Kennedy',
        'description': 3
      },
    ]
    return render(
      request,
      'events/listEvents.html',
      {
        'events': list
      }) 

def listEvents(request):
    list = Event.objects.all()
    return render(
        request,
        'events/listEvents.html',
        {
            'events' : list,
        })