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
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'John',"class": "form-control", 'id': 'firstname',
            }
        ),
        required=True
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Doe',"class": "form-control", 'id': 'lastname',
            }
        ),
        required=True
    )
    surname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Doe',"class": "form-control", 'id': 'surname',
                
            }
        ),
        required=False 
    )
    
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'JohnDoe',"class": "form-control", 'id': 'username',
            }
        ),
        required=True
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
        ),
        required=True
    )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'name@student.example.com',"class": "form-control", 'id': 'email'
            }
        ),
        required=True
    )
    student_id = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Student ID', "class": "form-control", 'id': 'student_id'}
        ),
        required=True
    )
    phone_number = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Phone Number', "class": "form-control", 'id': 'phone_number'}
        ),
        required=True
    )
    

    class Meta:
        model = User
        # fields = ('username', 'email', 'password1', 'password2','is_student')
        fields = ('first_name', 'last_name', 'surname', 'username', 'email', 'student_id', 'phone_number', 'password1', 'password2','is_student')