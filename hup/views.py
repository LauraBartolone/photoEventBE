from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
# Create your views here.

class BaseModelViewSet(ModelViewSet):
    """
        Parent Class for API
    """
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication]
    pass


class ProtectedBaseModelViewSet(ModelViewSet):
    """
        Parent Class for API
    """
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]