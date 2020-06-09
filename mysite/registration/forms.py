from django import forms
from django.contrib.auth.forms import UserCreationForm,PasswordResetForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(widget = forms.EmailInput(attrs={'class':'form-control form-control-sm','placeholder':'Enter your real gmail(google account only)else you wont be able to reset the password'}))

    class Meta():
        model = User
        fields = ('username','email','password1','password2')

    def __init__(self,*args,**kwargs):
        super(RegistrationForm,self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control form-control-sm'
        self.fields['username'].widget.attrs['placeholder'] = 'Do not enter your real name'
        self.fields['password1'].widget.attrs['class'] = 'form-control form-control-sm'
        self.fields['password1'].widget.attrs['placeholder'] = 'Set up a strong password .eg kh#w/72:r+ra'

        self.fields['password2'].widget.attrs['class'] = 'form-control form-control-sm'
