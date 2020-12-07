from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label='Email Address')
#możemy dodać tutaj jaką chcemy zmienna i następnie załączyć ją do class Meta: fields =

    class Meta:
        model = User
        fields = ['username','email','password1','password2']




class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(label='Email Address')

    class Meta:
        model = User
        fields = ['username','email']


class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['image']