from django import forms

class UserForm(forms.Form):
    username = forms.CharField(label='New User', max_length=200)
