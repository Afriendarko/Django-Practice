from django import forms


class NameForm2(forms.Form):
    your_name = forms.CharField(label='Your name',
                               max_length=15)