# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-12 09:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_auto_20171002_0848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abou',
            name='title',
            field=models.CharField(max_length=210),
        ),
    ]
