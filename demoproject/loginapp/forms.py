from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


class login_form(AuthenticationForm):
    class Meta:
        model = User
        fields = ["username", ]



# class login_form(forms.Form):
#     username = forms.CharField(label="")
#     password = forms.CharField(label="", widget=forms.PasswordInput)
