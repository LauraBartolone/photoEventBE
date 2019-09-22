from __future__ import unicode_literals
from django.conf.urls import url, include
from rest_framework import routers
from events.views import BackendEventModelViewSet
from events.views import BackendPhotoModelViewSet


router_events = routers.DefaultRouter()
router_events.register(r'events', BackendEventModelViewSet)
router_events.register(r'photoes', BackendPhotoModelViewSet)

urlpatterns = [
    url(r'^', include(router_events.urls)),
]