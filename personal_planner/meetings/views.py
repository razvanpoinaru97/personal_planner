from django.shortcuts import redirect, render, get_object_or_404
from django.forms import modelform_factory

from meetings.models import Meeting, Room

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def detail(request, id):
    # meeting = Meeting.objects.get(pk=id)
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, "meetings/detail.html", {"meeting": meeting})
    # ...

def meetings(request):
    return render(request, "meetings/meetings.html", {"meetings": Meeting.objects.all(), "num_meetings": Meeting.objects.count()})

MeetingForm = modelform_factory(Meeting, exclude=[])

def new(request):
    return render(request, "meetings/new.html", {"rooms": Room.objects.all()})

@csrf_exempt
def create_meeting(request):
    if request.method == "POST":
        title = request.POST['title']
        room = request.POST['room']
        print(f"Title: {title}, Room: {room}")
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("meetings")
    else:
        form = MeetingForm()
        return render(request, "meetings/new.html", {"form": form, "rooms": Room.objects.all()})