# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-27 19:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0003_user_friends_with'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='friends_with',
            field=models.ManyToManyField(blank=True, null=True, related_name='_user_friends_with_+', to='login_app.User'),
        ),
    ]