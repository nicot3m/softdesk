# Generated by Django 3.2.2 on 2021-05-13 18:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk', '0002_auto_20210512_2058'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]