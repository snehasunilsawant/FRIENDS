# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-27 18:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0002_auto_20170927_1013'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='friends_with',
            field=models.ManyToManyField(related_name='_user_friends_with_+', to='login_app.User'),
        ),
    ]
