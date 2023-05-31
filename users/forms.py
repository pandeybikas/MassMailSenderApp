from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
class SignupForm(UserCreationForm):
    username = forms.CharField(
        label= 'Username',
        widget= forms.TextInput(attrs={
            'class' : 'form-control',
            'type' : 'text'
        })
    )
    email = forms.EmailField(
        label= 'Email',
        widget= forms.EmailInput(attrs={
            'class' : 'form-control',
            'type' : 'email'
        })
    )
    password1 = forms.CharField(
        label= 'Password',
        widget= forms.PasswordInput(attrs={
            'class' : 'form-control',
            'type' : 'password'
        })
    )
    password2 = forms.CharField(
        label= 'Confirm Password',
        widget= forms.PasswordInput(attrs={
            'class' : 'form-control',
            'type' : 'password'
        })
    )
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProfileModelForm(forms.ModelForm):
    name = forms.CharField(
        label= 'Full Name',
        widget= forms.TextInput(attrs={
            'class' : 'form-control',
            'type' : 'text'
        })
    )
    company = forms.CharField(
        label= 'Company Name',
        widget= forms.TextInput(attrs={
            'class' : 'form-control',
            'type' : 'text'
        })
    )
    phone_number = forms.CharField(
        label= 'Phone Number',
        widget= forms.NumberInput(attrs={
            'class' : 'form-control',
            'type' : 'number'
        })
    )
    image = forms.FileField(
        label= 'Upload Image',
        widget= forms.FileInput(attrs={
            'class' : 'form-control',
            'type' : 'file',
            
        })
    )
    bio = forms.CharField(
        label= 'About Yourself',
        widget= forms.Textarea(attrs={
            'class' : 'form-control',
            'type' : 'text',
            
        })
    )
    class Meta:
        model = Profile
        fields = ['name', 'company', 'phone_number', 'image', 'bio']
        exclude= ['user']
