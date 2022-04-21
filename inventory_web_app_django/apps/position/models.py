from django.db import models

from apps.item.models import Item
from apps.department.models import Department
from apps.location.models import Location
from apps.account.models import Account


class Position(models.Model):
    #Relation Fields
    department = models.ForeignKey(Department, related_name="position_department", on_delete=models.PROTECT, null=True, blank=True)
    location = models.ForeignKey(Location, related_name="position_location", on_delete=models.PROTECT, null=True, blank=True)
    created_by = models.ForeignKey(Account, related_name="position_created_by", on_delete=models.PROTECT, null=True, blank=True)
    updated_by = models.ForeignKey(Account, related_name="position_updated_by", on_delete=models.PROTECT, null=True, blank=True)

    #Static Fields
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(max_length=1000, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.name
    
    def get_created_by(self):
        return self.created_by.first_name + " " + self.created_by.last_name

    def get_updated_by(self):
        return self.updated_by.first_name + " " + self.updated_by.last_name

class PositionItem(models.Model):
    item = models.ForeignKey(Item, related_name ="position_item", on_delete=models.PROTECT)
    position = models.ForeignKey(Position, related_name="items", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.item.name