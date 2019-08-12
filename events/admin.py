# -*- coding: utf-8 -*-
"""
    Admin for Events
"""
from __future__ import unicode_literals
from django.contrib import admin

from events.models import Event, Board
from hup.admin import BaseAdmin

# Register your models here.


class AdminEvent(BaseAdmin):
    """
        Admin for Event
    """
    list_display = BaseAdmin.list_display + ['date'] + ['name'] + ['note']


class AdminBoard(BaseAdmin):
    """
        Admin for Event
    """
    list_display = BaseAdmin.list_display


admin.site.register(Event, AdminEvent)
admin.site.register(Board, AdminBoard)