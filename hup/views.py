from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
# Create your views here.

class BaseModelViewSet(ModelViewSet):
    """
        Parent Class for API
    """
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication]
    pass
