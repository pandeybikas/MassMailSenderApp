from django import forms 
from .models import EmailList

class EmailModelForm(forms.ModelForm):
    name = forms.CharField(
       
        widget= forms.TextInput(attrs={
            'class' : 'form-control',
            'placeholder' : 'full name'
        })
    )
    email = forms.EmailField(
        
        widget= forms.EmailInput(attrs={
            'class' : 'form-control mx-3',
            'placeholder' : 'email'
        })
    )
    class Meta:
        model = EmailList
        fields = ['name', 'email']
        exclude= ['sender', 'subject', 'attachment', 'email_body']