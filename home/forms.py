from django import forms
from django.contrib.auth.models import User


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(label='Your Email', required=True)
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name' )
    class Meta:
        model = User
        fields = [ 'email', 'first_name', 'last_name']
        