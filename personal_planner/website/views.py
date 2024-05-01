from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse

from meetings.models import Meeting

# Create your views here.

def welcome(request):
    meetings = Meeting.objects.all()
    return render(request, "website/welcome.html", {"meetings": meetings, "num_meetings": Meeting.objects.count()})

def date(request):
    return HttpResponse("This page was served at " + str(datetime.now()))

def about(request):
    return HttpResponse("This is a personal planner application. One of the best we have ever seen!")