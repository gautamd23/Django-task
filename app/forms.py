from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User

# Create your views here.



class RegistrationForm(UserCreationForm):
    class Meta:
        model= User
        fields= ('username','email','password1','password2')



class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
