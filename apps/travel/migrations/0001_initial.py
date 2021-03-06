# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-27 19:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Users')),
            ],
        ),
        migrations.CreateModel(
            name='Schedules',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='travel_destination', to='travel.Plans')),
                ('end_date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='end', to='travel.Plans')),
                ('start_date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='start', to='travel.Plans')),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Users')),
            ],
        ),
    ]
