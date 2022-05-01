from django import forms
from django.forms import ModelForm
from .models import Users


class RegisterForm(ModelForm):
    username = forms.TextInput()
    email = forms.EmailField()
    password = forms.PasswordInput()
    # create_date = forms.DateTimeField()
    class Meta:
        model = Users
        fields = ['username','email','password']