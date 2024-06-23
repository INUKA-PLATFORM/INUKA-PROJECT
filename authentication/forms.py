from django import forms
from . models import *
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

# validations
def validate_pdf(file):
    if not file.name.endswith('.pdf'):
        raise ValidationError("Only PDF files are allowed.")
    if file.content_type != 'application/pdf':
        raise ValidationError("Only PDF files are allowed.")

ACADEMIC_YEAR_SEMESTER_CHOICES = [
    ('Year 1 Semester 1', 'Year 1 Semester 1'),
    ('Year 1 Semester 2', 'Year 1 Semester 2'),
    ('Year 2 Semester 1', 'Year 2 Semester 1'),
    ('Year 2 Semester 2', 'Year 2 Semester 2'),
    ('Year 3 Semester 1', 'Year 3 Semester 1'),
    ('Year 3 Semester 2', 'Year 3 Semester 2'),
    ('Year 4 Semester 1', 'Year 4 Semester 1'),
    ('Year 4 Semester 2', 'Year 4 Semester 2'),
]

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
    year_of_study = forms.ChoiceField(
        choices=ACADEMIC_YEAR_SEMESTER_CHOICES,
        widget=forms.Select(
            attrs={'class': 'form-select', 'id': 'year_of_study'}
        ),
        required=True
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
    student_id_number = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Student ID', "class": "form-control", 'id': 'student_id_number'}
        ),
        required=True
    )
    phone_number = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Phone Number', "class": "form-control", 'id': 'course'}
        ),
        required=True
    )
    guardian_contacts = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Guardian Phone No', "class": "form-control", 'id': 'guardian'}
        ),
        required=True
    )

    course = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Bsc Computer Science', "class": "form-control", 'id': 'course'}
        ),
        required=True
    )
    student_id = forms.FileField(
        widget=forms.FileInput(
            attrs={'placeholder': 'Attach ID card', "class": "form-control", 'id': 'student_id'}
        ),validators=[validate_pdf],
        required=True
    )
    passport_photo = forms.FileField(
        widget=forms.FileInput(
            attrs={'placeholder': 'Attach passport', "class": "form-control", 'id': 'passport_photo'}
        ),
        required=True
    )
    national_id= forms.FileField(
        widget=forms.FileInput(
            attrs={'placeholder': 'National ID card', "class": "form-control", 'id': 'national_id'}
        ),validators=[validate_pdf],
        required=True
    )
    financial_statements= forms.FileField(
        widget=forms.FileInput(
            attrs={'placeholder': 'Financial statements', "class": "form-control", 'id': 'financial_statements'}
        ),validators=[validate_pdf],
        required=True
    )
    letter_of_recommendation= forms.FileField(
        widget=forms.FileInput(
            attrs={'placeholder': 'Recommendation Letter', "class": "form-control", 'id': 'letter_of_recommendation'}
        ),validators=[validate_pdf],
        required=True
    )
    reason_for_application = forms.CharField(
        widget=forms.Textarea(
            attrs={'placeholder': '--- Type a Reason for application ---', 'class': 'form-control', 'id': 'reason_for_application'}
        ),
        required=True
    )
    
    

    class Meta:
        model = User
        # fields = ('username', 'email', 'password1', 'password2','is_student')
        fields = ('first_name', 'last_name', 'surname', 'username', 'email', 'student_id_number', 'phone_number', 'password1', 'password2','is_student','student_id',  'national_id', 
            'passport_photo', 'course', 'year_of_study', 'financial_statements', 
            'guardian_contacts', 'reason_for_application', 
            'letter_of_recommendation')