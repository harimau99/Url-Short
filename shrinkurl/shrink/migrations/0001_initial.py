# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-23 06:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='URLs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shrinkedURL', models.CharField(max_length=50)),
                ('targetURL', models.CharField(max_length=2083)),
            ],
        ),
    ]