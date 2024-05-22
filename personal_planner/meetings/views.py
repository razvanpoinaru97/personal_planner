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
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("meetings")
    else:
        form = MeetingForm()
    return render(request, "meetings/new.html", {"form": form})

    
def edit(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    if request.method == "POST":
        form = MeetingForm(request.POST, instance=meeting)
        if form.is_valid():
            form.save()
            return redirect("detail", id=id)
    else:
        form = MeetingForm(instance=meeting)
    return render(request, "meetings/edit.html", {"form": form, "meeting": meeting})

def delete(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    if (request.method == "POST"):
        meeting.delete()
        return redirect("meetings")
    else:
        return render(request, "meetings/confirm_delete.html", {"meeting": meeting})