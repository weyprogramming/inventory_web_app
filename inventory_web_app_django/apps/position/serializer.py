from rest_framework import serializers

from .models import Position, PositionItem
from apps.location.models import Location

from apps.item.models import Item
from apps.item.serializer import ItemSerializer

class PositionItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PositionItem
        fields = [
            'id',
            'item',
            'position',
            'quantity',
        ]

class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = [
            'id',
            'items',
            'department',
            'location',
            'created_by',
            'updated_by',
            'name',
            'description',
            'created_at',
            'updated_at',
        ]


class PositionDetailSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)
    updated_by = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Position
        fields = [
            'id',
            'items',
            'department',
            'location',
            'created_by',
            'updated_by',
            'name',
            'description',
            'created_at',
            'updated_at',
        ]
        depth=3
        