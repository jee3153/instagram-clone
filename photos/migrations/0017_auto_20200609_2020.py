# Generated by Django 3.0.6 on 2020-06-09 20:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('photos', '0016_auto_20200607_1640'),
    ]

    operations = [
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likers', models.ManyToManyField(related_name='likers', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='photo',
            name='tagperson',
            field=models.ManyToManyField(related_name='tagged', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Tagged',
        ),
        migrations.AddField(
            model_name='likes',
            name='photo',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='like', to='photos.Photo'),
        ),
    ]
