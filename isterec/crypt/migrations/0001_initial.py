# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-25 18:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UploadFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('rollno', models.CharField(default='', max_length=15)),
                ('mobileno', models.CharField(default='', max_length=20)),
                ('email', models.CharField(default='', max_length=50)),
                ('body', models.TextField(default='')),
                ('file', models.FileField(upload_to='files/%Y/%m/%d')),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]