# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-11-07 18:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Merit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session', models.CharField(max_length=100)),
                ('level', models.CharField(max_length=20)),
                ('student_name', models.CharField(max_length=100)),
                ('cgpa', models.FloatField()),
                ('position', models.PositiveIntegerField()),
               
            ],
        ),
    ]
