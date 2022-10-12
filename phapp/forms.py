from django import forms
from . models import Customer

class SignupForm(forms.ModelForm):
    Password=forms.CharField(widget=forms.PasswordInput,max_length=8)
    ConfirmPassword=forms.CharField(widget=forms.PasswordInput,max_length=8)
    class Meta():
        model=Customer
        fields='__all__'

class LoginForm(forms.ModelForm):
    Password:forms.CharField(widget=forms.PasswordInput,max_length=8)
    class Meta():
        model=Customer
        fields=("Email","Password")

