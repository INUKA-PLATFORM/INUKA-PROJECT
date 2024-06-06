from django import forms
from . models import *
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control", 'id': 'username',
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control", 'data-toggle': 'password',
                'id': 'password', "style": 'height:5vh;'
            }
        )
    )


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'JohnDoe',"class": "form-control", 'id': 'username',
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control", 'data-toggle': 'password',
                'id': 'password',
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control", 'data-toggle': 'password',
                'id': 'password'

            }
        )
    )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'name@student.example.com',"class": "form-control", 'id': 'email'
            }
        )
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2','is_student')