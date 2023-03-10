# Generated by Django 4.1.2 on 2023-03-10 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduledTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.CharField(default=0, max_length=255, unique=True)),
                ('status', models.CharField(default=0, max_length=50)),
                ('result', models.TextField(blank=True, default='', null=True)),
                ('date_done', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
