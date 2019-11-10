from django.db import models

# Create your models here.
from operator import attrgetter

from django.db import models
from autoslug import AutoSlugField
from model_utils.models import TimeStampedModel

# Create your models here.
from django.db import models

from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit, ResizeToFill
from imagekit.models import ImageSpecField

from django.contrib.auth.models import User


class Board(models.Model):

    @classmethod
    def get_new(cls):
        return cls.objects.create().id


class BoardMessage(models.Model):

    content = models.TextField(max_length=3000, blank=False, null=False)
    user = models.ForeignKey(User, blank=False, null=True, on_delete=models.SET_NULL)
    board = models.ForeignKey(Board, blank=False, null=False, on_delete=models.CASCADE)


class Category(models.Model):
    WEDDING = 'wedding'
    BIRTHDAY = 'birthday'
    GRADUATE = 'graduate'
    HOLY = 'wedding'
    PARTY = 'wedding'
    OTHER = 'other'

    CATEGORIES = [
        (WEDDING, 'wedding'),
        (BIRTHDAY, 'birthday'),
        (GRADUATE, 'graduate'),
        (HOLY, 'holy'),
        (PARTY, 'party'),
        (OTHER, 'other'),
    ]
    name = models.CharField(blank=False, null=False, choices=CATEGORIES, default=OTHER, max_length=15)


class Event(models.Model):
    image = ProcessedImageField(upload_to='events/background_images/%Y/%m/%d/',
                                   processors=[ResizeToFit(400, 400)],
                                   blank=True, null=True
                               )
    AUTOSLUG_FIELDS = 'name'
    name = models.CharField(max_length=255, blank=False, null=False)
    date = models.DateField(blank=False, null=False)
    note = models.CharField(max_length=255, blank=True, null=True)
    code = AutoSlugField(populate_from='name', max_length=7, unique=True)
    board = models.OneToOneField(Board, default=Board.get_new, on_delete=models.SET_DEFAULT)
    category = models.ForeignKey(Category, blank=False, null=False, on_delete=models.SET_DEFAULT, default=6)
    isPublic = models.BooleanField(default=False)
    user = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE)


class Photo(models.Model):

    image = ProcessedImageField(upload_to='events/background_images/%Y/%m/%d/',
                                blank=True, null=True,
                                format='JPEG',
                                options={'quality': 30}
                                )
    preview = ImageSpecField(source='image',
                                 processors=[ResizeToFill(140, 160)],
                                 format='JPEG',
                                 options={'quality': 90})

    user = models.ForeignKey(User, blank=False, null=True, on_delete=models.SET_NULL)
    event = models.ForeignKey(Event, blank=False, null=False, on_delete=models.CASCADE)


class Like(models.Model):
    photo = models.ForeignKey(Photo, blank=False, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, blank=False, null=True, on_delete=models.SET_NULL)





