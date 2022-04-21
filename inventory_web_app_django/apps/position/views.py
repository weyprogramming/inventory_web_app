from django.shortcuts import render
from rest_framework import viewsets

from .serializer import PositionDetailSerializer, PositionSerializer, PositionItemSerializer
from .models import Position, PositionItem

from django.core.exceptions import PermissionDenied

class PositionDetailViewset(viewsets.ModelViewSet):
    serializer_class = PositionDetailSerializer
    queryset = Position.objects.all()

    def get_queryset(self):
        return self.queryset.filter(department=self.request.user.department)
  
class PositionItemViewSet(viewsets.ModelViewSet):
    serializer_class = PositionItemSerializer
    queryset = PositionItem.objects.all()

class PositionViewSet(viewsets.ModelViewSet):
    serializer_class = PositionSerializer
    queryset = Position.objects.all()

    def get_queryset(self):
        return self.queryset.filter(department=self.request.user.department)

    def perform_update(self, serializer):
        return serializer.save(department=self.request.user.department, updated_by=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(department=self.request.user.department, updated_by=self.request.user)