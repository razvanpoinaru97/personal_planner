from datetime import time

from django.db import models

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name} in {self.location}"

class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField(default=time(9))
    description = models.TextField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + self.date.strftime(' on (%m/%d/%Y)') + self.time.strftime(' at %I:%M %p')
