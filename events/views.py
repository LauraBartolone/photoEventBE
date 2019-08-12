from django.shortcuts import render

# Create your views here
from hup.views import BaseModelViewSet
from events.models import Event
from events.serializer import BackendEventModelSerializer

class BackendEventModelViewSet(BaseModelViewSet):
    """
        Backend Artist Model View Set
    """

    queryset = Event.objects.all()
    serializer_class = BackendEventModelSerializer

