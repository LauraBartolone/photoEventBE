# Generated by Django 2.2.2 on 2019-11-10 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0014_event_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='code',
            field=models.CharField(default=None, max_length=5, unique=True),
        ),
    ]
