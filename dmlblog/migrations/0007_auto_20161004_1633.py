# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-04 15:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dmlblog', '0006_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/images'),
        ),
    ]
