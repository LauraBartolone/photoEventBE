from django.db import models

# Create your models here.
from operator import attrgetter

from django.db import models
from autoslug import AutoSlugField
from model_utils.models import TimeStampedModel

# Create your models here.
from django.db import models


class Board(models.Model):

    @classmethod
    def get_new(cls):
        return cls.objects.create().id


class Category(models.Model):
    WEDDING = 'wedding'
    BIRTHDAY = 'birthday'
    GRADUATE = 'graduate'
    HOLY = 'wedding'
    PARTY = 'wedding'
    OTHER = 'other'

    CATEGORIES = (
        (WEDDING, 'wedding'),
        (BIRTHDAY, 'birthday'),
        (GRADUATE, 'graduate'),
        (HOLY, 'wedding'),
        (PARTY, 'wedding'),
        (OTHER, 'other'),
    )
    name = models.CharField(blank=False, null=False, choices=CATEGORIES, default=OTHER, max_length=15)


class Event(models.Model):
    background_app_image = ProcessedImageField(upload_to='museums/background_app_images/%Y/%m/%d/',
                                               processors=[ResizeToFit(1980, 1080)],
                                               blank=True, null=True
                                               )
    AUTOSLUG_FIELDS = 'name'
    name = models.CharField(max_length=30, blank=False, null=False)
    date = models.DateField(blank=False, null=False)
    note = models.CharField(max_length=255, blank=True, null=True)
    code = AutoSlugField(populate_from='name', max_length=5, unique=True)
    board = models.OneToOneField(Board, default=Board.get_new, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, blank=False, null=False, on_delete=models.SET_DEFAULT, default=6)
    isPublic = models.BooleanField(default=False)


