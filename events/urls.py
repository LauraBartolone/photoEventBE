from __future__ import unicode_literals
from django.conf.urls import url, include
from rest_framework import routers
from events.views import BackendEventModelViewSet

router_events = routers.DefaultRouter()
router_events.register(r'events', BackendEventModelViewSet)

urlpatterns = [
    url(r'^', include(router_events.urls)),
]