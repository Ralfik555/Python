from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
