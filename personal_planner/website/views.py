from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def welcome(request):
    return HttpResponse("Welcome to the Personal Planner!")

def date(request):
    return HttpResponse("This page was served at " + str(datetime.now()))

def about(request):
    return HttpResponse("This is a personal planner application. One of the best we have ever seen!")