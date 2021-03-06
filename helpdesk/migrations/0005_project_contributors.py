# Generated by Django 3.2.2 on 2021-05-18 08:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('helpdesk', '0004_auto_20210517_2051'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='contributors',
            field=models.ManyToManyField(related_name='_helpdesk_project_contributors_+', through='helpdesk.Contributor', to=settings.AUTH_USER_MODEL),
        ),
    ]
