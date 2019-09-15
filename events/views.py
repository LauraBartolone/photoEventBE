from django.shortcuts import render

# Create your views here
from hup.views import BaseModelViewSet, ProtectedBaseModelViewSet

from rest_framework import status
from rest_framework.response import Response

from events.models import Event
from events.serializer import BackendEventModelSerializer


class BackendEventModelViewSet(ProtectedBaseModelViewSet):
    """
        Event Model View Set
    """

    queryset = Event.objects.all()
    serializer_class = BackendEventModelSerializer

    def create(self, request, *args, **kwargs):
        """
            It overrides "create function" to create an event
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        user = request.user

        event_obj = dict()
        try:
            event_obj['user'] = user.id
        except AttributeError:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        event_obj['name'] = request.data.get('name')
        event_obj['date'] = request.data.get('date')
        event_obj['note'] = request.data.get('note')
        event_obj['category'] = request.data.get('category')
        event_obj['image'] = request.data.get('image')

        serializer_event = BackendEventModelSerializer(data=event_obj)
        if serializer_event.is_valid():
            serializer_event.save()

            return Response(serializer_event.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_event.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        """
            It overrides "create function" to create an event
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        user = request.user

        event_obj = dict()
        try:
            event_obj['user'] = user.id
        except AttributeError:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        event_obj['name'] = request.data.get('name')
        event_obj['date'] = request.data.get('date')
        event_obj['note'] = request.data.get('note')
        event_obj['category'] = request.data.get('category')
        event_obj['image'] = request.data.get('image')

        serializer_event = BackendEventModelSerializer(data=event_obj)
        if serializer_event.is_valid():
            serializer_event.save()

            return Response(serializer_event.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer_event.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        """

        :return:
        """
        queryset = super(BackendEventModelViewSet, self).get_queryset()
        user = self.request.user
        queryset = queryset.filter(user=user)
        return queryset