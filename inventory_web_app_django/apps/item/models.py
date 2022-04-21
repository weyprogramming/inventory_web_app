from django.db import models
from apps.department.models import Department
from apps.account.models import Account


class Item(models.Model):

    # Static Fields
    TOOL = "tool"
    CONSUMABLE = "consumable"

    CHOICES_TYPE = (
        (TOOL, "tool"),
        (CONSUMABLE, "consumable"),
    )
    
    name = models.CharField(max_length=255)
    item_type = models.CharField(max_length=20, choices=CHOICES_TYPE, default=CONSUMABLE)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    url = models.CharField(max_length=1000, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # Relation Fields
    department = models.ForeignKey(Department, related_name='department_items', on_delete=models.CASCADE, null=True, blank=True)
    created_by = models.ForeignKey(Account, related_name='account_created_items', on_delete=models.CASCADE, null=True, blank=True)
    updated_by = models.ForeignKey(Account, related_name='account_updated_items', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name