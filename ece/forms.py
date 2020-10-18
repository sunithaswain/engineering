from django import forms
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Registrationform(forms.Form):
    signin = forms.CharField(max_length=250)
    password = forms.CharField(max_length=250)

class Signinform(forms.Form):
    username = forms.CharField(max_length=250)
    password = forms.CharField(max_length=250)
    # Address=forms.CharField(max_length=250)
    # Mobilenumber=forms.CharField(max_length=250)
class changeform(forms.Form):
    oldpassword=forms.CharField(max_length=250)
    newpassword = forms.CharField(max_length=250)
class Uploadform(forms.Form):
    image = forms.ImageField()