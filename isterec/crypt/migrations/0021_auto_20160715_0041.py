# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-14 21:41
from __future__ import unicode_literals

import crypt.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypt', '0020_auto_20160710_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(upload_to=crypt.models.content_file_name),
        ),
    ]