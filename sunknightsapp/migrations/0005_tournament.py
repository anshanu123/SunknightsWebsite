# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-20 17:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sunknightsapp', '0004_remove_clanuser_is_manager'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField(max_length=500)),
                ('finished', models.BooleanField(default=False)),
            ],
        ),
    ]