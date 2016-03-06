# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('on', models.DateTimeField(auto_now_add=True)),
                ('text', models.CharField(max_length=100)),
                ('by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HashTag',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('image', models.ImageField(upload_to='uploads/')),
                ('place', models.CharField(max_length=100, default='none')),
                ('on', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(null=True, max_length=120)),
                ('cuisine', models.CharField(max_length=30, default='none', choices=[('African', 'African'), ('American', 'American'), ('Argentinian', 'Argentinian'), ('Brazilian', 'Brazilian'), ('Cajun', 'Cajun'), ('Caribbean', 'Caribbean'), ('Chinese', 'Chinese'), ('Cuban', 'Cuban'), ('EastIndian', 'EastIndian'), ('Egyptian', 'Egyptian'), ('Ethiopian', 'Ethiopian'), ('French', 'French'), ('Filipino', 'Filipino'), ('German', 'German'), ('Greek', 'Greek'), ('Hawaiian', 'Hawaiian'), ('Indonesian', 'Indonesian'), ('Italian', 'Italian'), ('Iranian', 'Iranian'), ('Irish', 'Irish'), ('Japanese', 'Japanese'), ('Korean', 'Korean'), ('Lebanese', 'Lebanese'), ('Mediterranean', 'Mediterranean'), ('Mexican', 'Mexican'), ('Mongolian', 'Mongolian'), ('Mughlai', 'Mughlai'), ('NorthIndian', 'NorthIndian'), ('Polish', 'Polish'), ('Portuguese', 'Portuguese'), ('Scottish', 'Scottish'), ('SeaFood', 'SeaFood'), ('Spanish', 'Spanish'), ('SouthIndian', 'SouthIndian'), ('Swedish', 'Swedish'), ('Thai', 'Thai'), ('Turkish', 'Turkish'), ('Vietnamese', 'Vietnamese'), ('WestIndian', 'WestIndian')])),
                ('pin_points', models.IntegerField(default=0)),
                ('points', models.IntegerField(default=0)),
                ('public', models.BooleanField(default=True)),
                ('by', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='photos_uploaded')),
                ('hash_tags', models.ManyToManyField(related_name='tagged_photos', to='photobucket.HashTag')),
                ('likers', models.ManyToManyField(related_name='photos_liked', to=settings.AUTH_USER_MODEL)),
                ('pinners', models.ManyToManyField(blank=True, related_name='photos_pinned', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='recipe_images/')),
                ('on', models.DateTimeField(auto_now_add=True)),
                ('cuisine', models.CharField(max_length=30, default='none', choices=[('African', 'African'), ('American', 'American'), ('Argentinian', 'Argentinian'), ('Brazilian', 'Brazilian'), ('Cajun', 'Cajun'), ('Caribbean', 'Caribbean'), ('Chinese', 'Chinese'), ('Cuban', 'Cuban'), ('EastIndian', 'EastIndian'), ('Egyptian', 'Egyptian'), ('Ethiopian', 'Ethiopian'), ('French', 'French'), ('Filipino', 'Filipino'), ('German', 'German'), ('Greek', 'Greek'), ('Hawaiian', 'Hawaiian'), ('Indonesian', 'Indonesian'), ('Italian', 'Italian'), ('Iranian', 'Iranian'), ('Irish', 'Irish'), ('Japanese', 'Japanese'), ('Korean', 'Korean'), ('Lebanese', 'Lebanese'), ('Mediterranean', 'Mediterranean'), ('Mexiacan', 'Mexiacan'), ('Mongolian', 'Mongolian'), ('Mughlai', 'Mughlai'), ('NorthIndian', 'NorthIndian'), ('Polish', 'Polish'), ('Portuguese', 'Portuguese'), ('Scottish', 'Scottish'), ('SeaFood', 'SeaFood'), ('Spanish', 'Spanish'), ('SouthIndian', 'SouthIndian'), ('Swedish', 'Swedish'), ('Thai', 'Thai'), ('Turkish', 'Turkish'), ('Vietnamese', 'Vietnamese'), ('WestIndian', 'WestIndian')])),
                ('title', models.TextField(max_length=100)),
                ('pin_points', models.IntegerField(default=0)),
                ('points', models.IntegerField(default=0)),
                ('ingredients', models.TextField(max_length=1000)),
                ('method', models.TextField(max_length=2000)),
                ('prep_time', models.DurationField(null=True, blank=True)),
                ('cook_time', models.DurationField()),
                ('by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('likers', models.ManyToManyField(null=True, related_name='recipe_liked', to=settings.AUTH_USER_MODEL)),
                ('pinners', models.ManyToManyField(null=True, blank=True, related_name='recipe_pinned', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe_Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('on', models.DateTimeField(auto_now_add=True)),
                ('text', models.CharField(max_length=100)),
                ('by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('recipe', models.ForeignKey(to='photobucket.Recipe')),
            ],
        ),
        migrations.CreateModel(
            name='Report_Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('on', models.DateTimeField(auto_now_add=True)),
                ('reason', models.CharField(max_length=30, default='none', choices=[('This photo is a spam or a scam', 'This photo is spam or a scam'), ('This photo puts people at risk', 'This photo puts people at risk'), ("This photo shouldn't be on foodchaps", "This photo shouldn't be on foodchaps")])),
                ('by', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='reported_photo')),
                ('photo', models.ForeignKey(to='photobucket.Photo')),
            ],
        ),
        migrations.CreateModel(
            name='Report_Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('on', models.DateTimeField(auto_now_add=True)),
                ('reason', models.CharField(max_length=40, default='none', choices=[('This recipe is a spam or a scam', 'This recipe is spam or a scam'), ('This recipe puts people at risk', 'This recipe puts people at risk'), ("This recipe shouldn't be on foodchaps", "This recipe shouldn't be on foodchaps")])),
                ('recipe', models.ForeignKey(to='photobucket.Recipe')),
                ('reportedby', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='reported_recipe')),
            ],
        ),
        migrations.AddField(
            model_name='recipe',
            name='reporters',
            field=models.ManyToManyField(null=True, through='photobucket.Report_Recipe', related_name='recipes_reported', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='photo',
            name='reporters',
            field=models.ManyToManyField(through='photobucket.Report_Photo', related_name='photos_reported', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='photo',
            name='user_tags',
            field=models.ManyToManyField(related_name='photos_tagged_in', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='photo',
            field=models.ForeignKey(to='photobucket.Photo'),
        ),
    ]
