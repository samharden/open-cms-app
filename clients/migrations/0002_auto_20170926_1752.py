# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 12:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clients', '0001_initial'),
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='assigned_to',
            field=models.ManyToManyField(related_name='account_assigned_to', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='account',
            name='billing_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='account_billing_address', to='common.Address'),
        ),
        migrations.AddField(
            model_name='account',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='account',
            name='shipping_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='account_shipping_address', to='common.Address'),
        ),
        migrations.AddField(
            model_name='account',
            name='teams',
            field=models.ManyToManyField(to='common.Team'),
        ),
    ]
