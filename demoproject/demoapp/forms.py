from django import forms
from django.forms import ModelForm
from .models import Musician1

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name',
                               max_length=100)

class mf(forms.ModelForm):
    class Meta:
        model = Musician1
        fields = "__all__"
