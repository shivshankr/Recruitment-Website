# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-02 11:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField()),
                ('is_correct', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ChargeRecData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('rollno', models.CharField(default='', max_length=15)),
                ('mobileno', models.CharField(default='', max_length=20)),
                ('email', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page', models.IntegerField()),
                ('question', models.TextField()),
                ('creation', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='charge.ChargeRecData'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='charge.Question'),
        ),
    ]
