# Generated by Django 2.2.5 on 2020-01-03 01:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='host',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
