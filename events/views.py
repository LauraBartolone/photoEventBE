import json

from django.shortcuts import render

# Create your views here
from rest_framework.status import HTTP_200_OK

from events.paginations import PhotoPagination, BoardMessagePagination
from hup.views import BaseModelViewSet, ProtectedBaseModelViewSet, BaseAPIView

from rest_framework import status
from rest_framework.response import Response

from events.models import Event, Photo, BoardMessage
from events.serializer import BackendEventModelSerializer, BackendPhotoModelSerializer, BackendBoardMessageSerializer, \
    BackendBoardMessageWithUserSerializer
from django.http import JsonResponse

from django.core import serializers

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


class BackendBoardMessageModelViewSet(ProtectedBaseModelViewSet):

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return BackendBoardMessageSerializer
        return BackendBoardMessageWithUserSerializer

    queryset = BoardMessage.objects.all()
    serializer_class = get_serializer_class
    pagination_class = BoardMessagePagination

    def get_queryset(self):
        """

        :return:
        """
        board = self.request.query_params.get('board', None)
        queryset = super(BackendBoardMessageModelViewSet, self).get_queryset()
        queryset = queryset.filter(board_id=board)
        return queryset.order_by('-pk')


class BackendPhotoModelViewSet(BaseModelViewSet):
    """
        Photo Model View Set
    """

    queryset = Photo.objects.all()
    serializer_class = BackendPhotoModelSerializer
    pagination_class = PhotoPagination

    def get_queryset(self):
        """

        :return:
        """
        queryset = super(BackendPhotoModelViewSet, self).get_queryset()
        event_code = self.request.query_params.get('event', None)
        queryset = queryset.filter(event__code=event_code)
        event = Event.objects.filter(code = event_code).exists()

        if event:
            return queryset.order_by('pk')


class BackendEventAPIView(BaseAPIView):
    """
    """

    def get(self, request, code):
        """

        :param request:
        :param code: can be matri, mat-01
        :return:
        """

        event_exist = Event.objects.filter(code=code).exists()
        event = Event.objects.filter(code=code).get()

        if event_exist:
            event_obj = dict()
            event_obj['id'] = event.id
            event_obj['board'] = event.board_id
            event_obj['status'] = 200
            return Response(event_obj, status=HTTP_200_OK)
        else:
            return Response({'status': 400}, status=status.HTTP_400_BAD_REQUEST)