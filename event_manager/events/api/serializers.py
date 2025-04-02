from rest_framework import serializers
from events.models import Category, Event


class EventInlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ["id", "name", "author"]


class CategorySerializer(serializers.ModelSerializer):
    """
    Model-Serializer baut aus Model Serialzer
    """
    # Events im Lesemodus in die Kategorien rein-serialisieren
    events = EventInlineSerializer(many=True, read_only=True)

    class Meta:
        model = Category 
        fields = "__all__"