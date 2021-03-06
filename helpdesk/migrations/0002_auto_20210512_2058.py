# Generated by Django 3.2.2 on 2021-05-12 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issue',
            name='desc',
        ),
        migrations.AddField(
            model_name='issue',
            name='description',
            field=models.CharField(blank=True, max_length=2048),
        ),
        migrations.AlterField(
            model_name='project',
            name='type',
            field=models.CharField(choices=[('backend', 'backend'), ('frontend', 'frontend'), ('Android', 'Android'), ('iOS', 'iOS')], default='backend', max_length=8),
        ),
    ]
