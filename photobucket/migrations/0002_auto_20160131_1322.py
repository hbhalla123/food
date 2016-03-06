# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photobucket', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report_photo',
            old_name='by',
            new_name='reportedby',
        ),
        migrations.RenameField(
            model_name='report_recipe',
            old_name='reportedby',
            new_name='by',
        ),
    ]
