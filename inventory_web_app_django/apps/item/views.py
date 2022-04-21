
from django.shortcuts import render
from rest_framework import viewsets
import json


from apps.account.models import Account

from .serializer import ItemSerializer
from .models import Item

from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.http import JsonResponse

class ItemViewset(viewsets.ModelViewSet):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()

    def get_queryset(self):
        print(self.request.user)
        return self.queryset.filter(department=self.request.user.department)

    def perform_create(self, serializer):
        serializer.save(
            created_by = self.request.user,
            department = self.request.user.department,
            updated_by = self.request.user,
        )

    def perform_update(self, serializer):
        obj = self.get_object()

        if self.request.user.department != obj.department:
            raise PermissionDenied("Wrong Department")

        serializer.save(
            department = self.request.user.department,
            updated_by = self.request.user
        )

class ItemSearchViewset(viewsets.ModelViewSet):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()

    def get_queryset(self):
        query = self.request.GET['query']

        return self.queryset.filter(department=self.request.user.department).filter((Q(name__icontains=query) | Q(description__icontains=query)))               