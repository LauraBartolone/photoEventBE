# Generated by Django 2.2.2 on 2019-09-29 07:36

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0010_photo_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='code',
            field=autoslug.fields.AutoSlugField(editable=False, max_length=7, populate_from='name', unique=True),
        ),
    ]
