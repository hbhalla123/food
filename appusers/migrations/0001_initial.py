# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.auth.models
import django.utils.timezone
import datetime
import django.core.validators
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=30, error_messages={'unique': 'A user with that username already exists.'}, verbose_name='username', unique=True, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')])),
                ('first_name', models.CharField(blank=True, verbose_name='first name', max_length=30)),
                ('last_name', models.CharField(blank=True, verbose_name='last name', max_length=30)),
                ('email', models.EmailField(blank=True, verbose_name='email address', max_length=254)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('profile_pic', models.ImageField(blank=True, upload_to='profile_pics/')),
                ('gender', models.CharField(default='M', max_length=1, choices=[('M', 'Male'), ('F', 'Female')])),
                ('phone', models.CharField(blank=True, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")], max_length=15)),
                ('dob', models.DateField(blank=True, null=True)),
                ('street_address', models.CharField(blank=True, null=True, max_length=100)),
                ('city', models.CharField(blank=True, null=True, max_length=255)),
                ('pincode', models.CharField(default='0000000', max_length=8)),
                ('email_id', models.EmailField(max_length=255)),
                ('following', models.ManyToManyField(related_name='followers', to=settings.AUTH_USER_MODEL)),
                ('groups', models.ManyToManyField(related_name='user_set', to='auth.Group', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', blank=True, related_query_name='user', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_name='user_set', to='auth.Permission', help_text='Specific permissions for this user.', blank=True, related_query_name='user', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Connection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('user1', models.ForeignKey(related_name='connection_user1', to=settings.AUTH_USER_MODEL)),
                ('user2', models.ForeignKey(related_name='connection_user2', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Connection',
                'verbose_name_plural': 'Connections',
            },
        ),
        migrations.CreateModel(
            name='cuisine_choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('cuisines', models.CharField(default='NorthIndian', max_length=25, choices=[('African', 'African'), ('American', 'American'), ('Argentinian', 'Argentinian'), ('Brazilian', 'Brazilian'), ('Cajun', 'Cajun'), ('Caribbean', 'Caribbean'), ('Chinese', 'Chinese'), ('Cuban', 'Cuban'), ('EastIndian', 'EastIndian'), ('Egyptian', 'Egyptian'), ('Ethiopian', 'Ethiopian'), ('French', 'French'), ('Filipino', 'Filipino'), ('German', 'German'), ('Greek', 'Greek'), ('Hawaiian', 'Hawaiian'), ('Indonesian', 'Indonesian'), ('Italian', 'Italian'), ('Iranian', 'Iranian'), ('Irish', 'Irish'), ('Japanese', 'Japanese'), ('Korean', 'Korean'), ('Lebanese', 'Lebanese'), ('Mediterranean', 'Mediterranean'), ('Mexican', 'Mexican'), ('Mongolian', 'Mongolian'), ('Mughlai', 'Mughlai'), ('NorthIndian', 'NorthIndian'), ('Polish', 'Polish'), ('Portuguese', 'Portuguese'), ('Scottish', 'Scottish'), ('SeaFood', 'SeaFood'), ('Spanish', 'Spanish'), ('SouthIndian', 'SouthIndian'), ('Swedish', 'Swedish'), ('Thai', 'Thai'), ('Turkish', 'Turkish'), ('Vietnamese', 'Vietnamese'), ('WestIndian', 'WestIndian')])),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('info', models.CharField(null=True, max_length=300)),
                ('recommended_dish', models.CharField(null=True, max_length=100)),
                ('fav_restro', models.CharField(null=True, max_length=100)),
                ('disliked_food', models.CharField(null=True, max_length=50)),
                ('liked_cuisine', models.ManyToManyField(related_name='liked_cuisinelist', to='appusers.cuisine_choice')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('activation_key', models.CharField(blank=True, max_length=40)),
                ('key_expires', models.DateTimeField(default=datetime.date(2015, 12, 22))),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'User profiles',
            },
        ),
        migrations.AlterUniqueTogether(
            name='connection',
            unique_together=set([('user1', 'user2')]),
        ),
    ]
