# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-31 10:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ig', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='title',
            new_name='username',
        ),
    ]
