# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-31 10:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ig', '0002_auto_20190731_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]