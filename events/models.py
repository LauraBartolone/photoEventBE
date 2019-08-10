from django.db import models

# Create your models here.
from operator import attrgetter

from django.db import models
from autoslug import AutoSlugField
from model_utils.models import TimeStampedModel

# Create your models here.
from django.db import models


def get_populate_from(instance):
    attrs = [attr.replace("__", ".") for attr in instance.AUTOSLUG_FIELDS]
    attrs_values = [attrgetter(attr)(instance) for attr in attrs]

    return "-".join(attrs_values)


class Board(models.Model):

    @classmethod
    def get_new(cls):
        return cls.objects.create().id


class Event(models.Model):
    # background_app_image = ProcessedImageField(upload_to='museums/background_app_images/%Y/%m/%d/',
    #                                            processors=[ResizeToFit(1980, 1080)],
    #                                            blank=True, null=True
    #                                            )
    AUTOSLUG_FIELDS = "name"
    name = models.CharField(max_length=30, blank=False, null=False)
    date = models.DateField(blank=False, null=False)
    note = models.CharField(max_length=255, blank=True, null=True)
    code = AutoSlugField(max_length=5, populate_from=get_populate_from, unique=True)
    board = models.OneToOneField(Board, default=Board.get_new, on_delete=models.CASCADE)
    # isPublic = models.BooleanField(default=False)
