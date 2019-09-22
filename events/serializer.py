from hup.serializers import BaseSerializer, Base64ImageField
from events.models import Event, Photo


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
