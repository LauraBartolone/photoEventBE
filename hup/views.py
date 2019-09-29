from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
# Create your views here.
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


class BaseModelViewSet(ModelViewSet):
    """
        Parent Class for APIsetti
    """
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication]
    pass


class ProtectedBaseModelViewSet(ModelViewSet):
    """
        Parent Class for API
    """
    permission_classes = [IsAuthenticated]
    authentication_classes = [JSONWebTokenAuthentication]


class BaseAPIView(APIView):
    """
        Parent Class for API View
    """