# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-13 11:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0014_remove_menuimage_menu_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menuimage',
            options={'verbose_name': 'MenuImage', 'verbose_name_plural': 'MenuImages'},
        ),
        migrations.AlterField(
            model_name='menuimage',
            name='restaurant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='menu_image', to='restaurant.Restaurant'),
        ),
    ]