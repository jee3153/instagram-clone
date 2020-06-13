# Generated by Django 3.0.6 on 2020-06-04 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_comment_mention'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created']},
        ),
        migrations.RemoveField(
            model_name='comment',
            name='is_liked',
        ),
        migrations.AddField(
            model_name='comment',
            name='like',
            field=models.IntegerField(default=0),
        ),
    ]
