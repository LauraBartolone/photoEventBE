# Generated by Django 2.2.2 on 2019-08-12 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='category',
            field=models.ForeignKey(default=6, on_delete=django.db.models.deletion.SET_DEFAULT, to='events.Category'),
        ),
    ]
