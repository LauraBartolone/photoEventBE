# Generated by Django 2.2.2 on 2019-11-10 18:36

from django.db import migrations, models
import events.models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0017_event_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='code',
            field=models.CharField(default=events.models.Event.f, max_length=5, null=True, unique=True),
        ),
    ]