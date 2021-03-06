# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-12-07 06:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('co_curricular', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archive',
            name='photo',
            field=models.ImageField(upload_to='CSE_BRUR/static/images/co_curricular/Archive'),
        ),
        migrations.AlterField(
            model_name='cse_club',
            name='photo',
            field=models.ImageField(upload_to='CSE_BRUR/static/images/co_curricular/Cse_club'),
        ),
        migrations.AlterField(
            model_name='events',
            name='banner_photo',
            field=models.ImageField(upload_to='CSE_BRUR/static/images/co_curricular/Events'),
        ),
        migrations.AlterField(
            model_name='game_achivement',
            name='photo',
            field=models.ImageField(upload_to='CSE_BRUR/static/images/co_curricular/Game_achivement'),
        ),
        migrations.AlterField(
            model_name='image',
            name='photo',
            field=models.ImageField(upload_to='CSE_BRUR/static/images/co_curricular/Image'),
        ),
    ]
