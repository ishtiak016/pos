from django import forms
from django.contrib.auth.models import User
from .models import profile
from django.contrib.auth.forms import UserCreationForm
class CreateUserFrom(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=['username','email','password1','password2']
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email']
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=profile
        fields=['address','phone','image']
