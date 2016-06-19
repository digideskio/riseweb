# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-05 18:51
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_remove_posts_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='publish',
            field=models.DateField(default=datetime.datetime(2016, 6, 5, 18, 51, 28, 828000, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='posts',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='%Y/%m/%d/'),
        ),
    ]
