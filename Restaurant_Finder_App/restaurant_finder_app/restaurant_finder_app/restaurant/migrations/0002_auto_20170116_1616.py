# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-16 16:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Days',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='available_days',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='available_time',
        ),
        migrations.AddField(
            model_name='openingtime',
            name='restaurant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurant.Restaurant'),
        ),
        migrations.DeleteModel(
            name='OpeningDaysModel',
        ),
        migrations.AddField(
            model_name='openingtime',
            name='available_days',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurant.Days'),
        ),
    ]
