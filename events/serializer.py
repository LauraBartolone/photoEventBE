from hup.serializers import BaseSerializer, Base64ImageField
from events.models import Event


class BackendEventModelSerializer(BaseSerializer):

    image = Base64ImageField(max_length=None, use_url=True, required=False, allow_null=True)

    class Meta:
        model = Event
        exclude = []