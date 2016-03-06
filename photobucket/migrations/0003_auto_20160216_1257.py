# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('photobucket', '0002_auto_20160131_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='likers',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='recipe_liked'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='pinners',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='recipe_pinned', blank=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='reporters',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='recipes_reported', through='photobucket.Report_Recipe'),
        ),
    ]
