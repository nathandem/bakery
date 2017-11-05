# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-01 11:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0004_stock'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sale',
            name='bread',
        ),
        migrations.AlterField(
            model_name='bread',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='bread',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='stock',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.DeleteModel(
            name='Sale',
        ),
    ]