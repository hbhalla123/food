from django import forms
from .models import *
from django.core import serializers
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from photobucket.models import *
from django.forms import ModelForm

class photoForm(ModelForm):
    class Meta:
        model = Photo
		fields = '__all__'
		exclude = ['by','on','likers']
        
