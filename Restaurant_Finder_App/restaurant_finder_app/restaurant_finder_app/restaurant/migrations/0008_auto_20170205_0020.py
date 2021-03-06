# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-05 00:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0007_auto_20170202_1522'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='restaurant_thumbnail_image',
            field=models.ImageField(default='images/thumbnails/restaurant_pic/no-name.jpg', upload_to='images/thumbnails/restaurant_pic/'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='restaurant_image',
            field=models.ImageField(default='images/restaurant_pic/no-name.jpg', upload_to='images/restaurant_pic/'),
        ),
    ]
