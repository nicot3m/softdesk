# Generated by Django 3.2.2 on 2021-05-10 19:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('description', models.CharField(blank=True, max_length=2048)),
                ('type', models.CharField(choices=[('Web', 'Web'), ('Android', 'Android'), ('iOS', 'iOS')], default='Web', max_length=7)),
                ('author_user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('desc', models.CharField(max_length=128)),
                ('tag', models.CharField(choices=[('Bug', 'Bug'), ('Task', 'Task'), ('Upgrade', 'Upgrade')], default='Bug', max_length=7)),
                ('priority', models.CharField(choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')], default='Low', max_length=6)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Open', 'Open'), ('Closed', 'Closed')], default='Pending', max_length=7)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('assignee_user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assignee_id', to=settings.AUTH_USER_MODEL)),
                ('author_user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='author_id', to=settings.AUTH_USER_MODEL)),
                ('project_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='helpdesk.project')),
            ],
        ),
        migrations.CreateModel(
            name='Contributor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.CharField(choices=[('None', 'None'), ('Read', 'Read'), ('All', 'All')], default='Read', max_length=4)),
                ('role', models.CharField(max_length=128)),
                ('project_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='helpdesk.project')),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=2048)),
                ('author_user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('issue_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='helpdesk.issue')),
            ],
        ),
    ]