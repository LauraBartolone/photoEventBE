# Generated by Django 2.2.2 on 2019-11-16 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0018_auto_20191110_1936'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='isPublic',
        ),
    ]
