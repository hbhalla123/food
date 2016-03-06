# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appusers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='liked_cuisine',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='favourite_cuisine',
            field=models.CharField(default='none', max_length=30, choices=[('African', 'African'), ('American', 'American'), ('Argentinian', 'Argentinian'), ('Brazilian', 'Brazilian'), ('Cajun', 'Cajun'), ('Caribbean', 'Caribbean'), ('Chinese', 'Chinese'), ('Cuban', 'Cuban'), ('EastIndian', 'EastIndian'), ('Egyptian', 'Egyptian'), ('Ethiopian', 'Ethiopian'), ('French', 'French'), ('Filipino', 'Filipino'), ('German', 'German'), ('Greek', 'Greek'), ('Hawaiian', 'Hawaiian'), ('Indonesian', 'Indonesian'), ('Italian', 'Italian'), ('Iranian', 'Iranian'), ('Irish', 'Irish'), ('Japanese', 'Japanese'), ('Korean', 'Korean'), ('Lebanese', 'Lebanese'), ('Mediterranean', 'Mediterranean'), ('Mexican', 'Mexican'), ('Mongolian', 'Mongolian'), ('Mughlai', 'Mughlai'), ('NorthIndian', 'NorthIndian'), ('Polish', 'Polish'), ('Portuguese', 'Portuguese'), ('Scottish', 'Scottish'), ('SeaFood', 'SeaFood'), ('Spanish', 'Spanish'), ('SouthIndian', 'SouthIndian'), ('Swedish', 'Swedish'), ('Thai', 'Thai'), ('Turkish', 'Turkish'), ('Vietnamese', 'Vietnamese'), ('WestIndian', 'WestIndian')]),
        ),
    ]
