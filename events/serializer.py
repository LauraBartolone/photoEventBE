from hup.serializers import BaseSerializer, Base64ImageField
from events.models import Event, Photo, BoardMessage
from rest_framework.fields import CurrentUserDefault
from rest_framework import serializers


class BackendEventModelSerializer(BaseSerializer):

    image = Base64ImageField(max_length=None, use_url=True, required=False, allow_null=True)

    class Meta:
        model = Event
        exclude = []


class BackendPhotoModelSerializer(BaseSerializer):
    image = Base64ImageField(max_length=None, use_url=True, required=False, allow_null=True)

    class Meta:
        model = Photo
        exclude = []


class BackendBoardMessageSerializer(BaseSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    class Meta:
        model = BoardMessage
        exclude = []
