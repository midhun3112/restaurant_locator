# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-18 12:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0008_auto_20170118_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='restaurant_image',
            field=models.ImageField(default='restaurant_pic_folder/None/no-img.jpg', upload_to='/images/restaurant_pic/'),
        ),
    ]
