from rest_framework import serializers
from events.models import Event


class BackendEventModelSerializer(serializers.ModelSerializer):

    # image = Base64ImageField(max_length=None, use_url=True)

    class Meta:
        model = Event
        exclude = []