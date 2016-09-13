from django import forms 

class CharacterForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=48)
    last_name = forms.CharField(label='Last Name', max_length=48)
