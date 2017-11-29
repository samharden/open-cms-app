# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-11-27 20:47
from __future__ import unicode_literals

import cases.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0004_uploadfile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadfile',
            name='case',
        ),
        migrations.AlterField(
            model_name='uploadfile',
            name='document',
            field=models.FileField(upload_to=cases.models.user_directory_path),
        ),
        migrations.AlterField(
            model_name='uploadfile',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cases.Case'),
        ),
    ]
