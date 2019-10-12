from __future__ import unicode_literals
from django.conf.urls import url, include
from rest_framework import routers
from events.views import BackendEventModelViewSet, BackendEventAPIView
from events.views import BackendPhotoModelViewSet, BackendBoardMessageModelViewSet


router_events = routers.DefaultRouter()
router_events.register(r'events', BackendEventModelViewSet)
router_events.register(r'photos', BackendPhotoModelViewSet)
router_events.register(r'board-messages', BackendBoardMessageModelViewSet)


urlpatterns = [
    url(r'^', include(router_events.urls)),
    url(r'^event/(?P<code>[\w-]{5,7})/$', BackendEventAPIView.as_view()),
]