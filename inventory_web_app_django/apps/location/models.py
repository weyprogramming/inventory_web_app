from pydoc import describe
from django.db import models
from apps.department.models import Department
from apps.account.models import Account

class Building(models.Model):
    name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Room(models.Model):
    name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=255)
    number = models.IntegerField()

    def __str__(self):
        return self.name

class Location(models.Model):

    building = models.ForeignKey(Building, related_name="location_building", on_delete=models.CASCADE)
    room = models.ForeignKey(Room, related_name="location_room", on_delete=models.CASCADE)
    department = models.ForeignKey(Department, related_name="location_department", on_delete=models.CASCADE)
    cabinet_number = models.IntegerField(blank=True, null=True)
    box_number = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.building.name + " / " + self.room.name
