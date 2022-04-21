from django.contrib import admin
from .models import Location, Building, Room

admin.site.register(Location)
admin.site.register(Building)
admin.site.register(Room)