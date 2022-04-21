from importlib.metadata import requires
from rest_framework import serializers

from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    #created_by = serializers.SerializerMethodField('get_created_by_name', read_only=True)
    #updated_by = serializers.SerializerMethodField('get_updated_by_name')
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Item
        fields = [
            "id",
            "name",
            "item_type",
            "description",
            "price",
            "url",
        ]

    #def get_created_by_name(self, Item):
    #   created_by_name = Item.created_by.first_name + " " + Item.created_by.last_name
    #   return created_by_name

    #def get_updated_by_name(self, Item):
    #    updated_by_name = Item.updated_by.first_name + " " + Item.updated_by.last_name
    #    return updated_by_name