from django.contrib import admin

# Register your models here.
# -*- coding: utf-8 -*-
"""
    Generics Admin
"""
from django.contrib import admin


class BaseAdmin(admin.ModelAdmin):
    """
        Base Admin
    """
    list_display = ['id']

