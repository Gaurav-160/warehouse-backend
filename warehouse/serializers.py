from rest_framework import serializers
from .models import Godown, Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class GodownSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)  # Include related items
    sub_godowns = serializers.SerializerMethodField()  # To include child godowns

    class Meta:
        model = Godown
        fields = ['id', 'name', 'parent_godown', 'items', 'sub_godowns']

    def get_sub_godowns(self, obj):
        # Get child godowns (sub-locations)
        child_godowns = Godown.objects.filter(parent_godown=obj)
        return GodownSerializer(child_godowns, many=True).data
