# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-30 18:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'default_related_name': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collection_name', models.CharField(max_length=255)),
            ],
            options={
                'default_related_name': 'collections',
            },
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurant_name', models.CharField(max_length=255)),
                ('restaurant_image', models.ImageField(default='restaurant_pic/images/no-name.jpg', upload_to='images/restaurant_pic/')),
            ],
            options={
                'default_related_name': 'restaurant',
            },
        ),
        migrations.CreateModel(
            name='RestaurantTiming',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('restaurant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='restaurant_timing', to='restaurant.Restaurant')),
            ],
            options={
                'default_related_name': 'restaurant_timing',
            },
        ),
        migrations.CreateModel(
            name='WeekDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=255)),
            ],
            options={
                'default_related_name': 'week_day',
            },
        ),
        migrations.AddField(
            model_name='restauranttiming',
            name='working_days',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='restaurant_timing', to='restaurant.WeekDay'),
        ),
        migrations.AddField(
            model_name='collection',
            name='restaurant',
            field=models.ManyToManyField(related_name='collections', to='restaurant.Restaurant'),
        ),
        migrations.AddField(
            model_name='category',
            name='restaurant',
            field=models.ManyToManyField(related_name='categories', to='restaurant.Restaurant'),
        ),
    ]
