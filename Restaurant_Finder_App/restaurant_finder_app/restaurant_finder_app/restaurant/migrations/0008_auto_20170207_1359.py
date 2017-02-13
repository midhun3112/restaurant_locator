# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-07 13:59
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0007_auto_20170202_1522'),
    ]

    operations = [
        migrations.CreateModel(
            name='CostForTwo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost_for_two', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name': 'CostForTwo',
                'verbose_name_plural': 'CostForTwo',
                'default_related_name': 'cost_for_two',
            },
        ),
        migrations.CreateModel(
            name='Cuisine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuisine_name', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name': 'Cuisine',
                'verbose_name_plural': 'Cusines',
                'default_related_name': 'cuisine',
            },
        ),
        migrations.CreateModel(
            name='EstablishmentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_establishment', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name': 'EstablishmentType',
                'verbose_name_plural': 'EstablishmentTypes',
                'default_related_name': 'establishment_type',
            },
        ),
        migrations.AddField(
            model_name='restaurant',
            name='address_1',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='address_2',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='city',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='country',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='has_outdoor_seating',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='is_alcohol_served',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='is_buffet_offered',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='is_credit_cards_accepted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='is_pure_veg',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='is_wifi_offered',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='locality',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='phone_number_1',
            field=models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='phone_number_2',
            field=models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='pincode',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restaurant',
            name='state',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='establishmenttype',
            name='restaurant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='establishment_type', to='restaurant.Restaurant'),
        ),
        migrations.AddField(
            model_name='cuisine',
            name='restaurant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cuisine', to='restaurant.Restaurant'),
        ),
        migrations.AddField(
            model_name='costfortwo',
            name='restaurant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cost_for_two', to='restaurant.Restaurant'),
        ),
    ]