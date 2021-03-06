# Generated by Django 3.0.5 on 2020-04-30 11:53

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('photos', '0003_auto_20200430_1018'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photo',
            options={'ordering': ['created']},
        ),
        migrations.AddField(
            model_name='photo',
            name='tagged',
            field=models.ManyToManyField(related_name='tagged', to=settings.AUTH_USER_MODEL),
        ),
    ]
