from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignupForm(UserCreationForm):

    email = forms.CharField(max_length= 30, required=True, strip= True,)

    class Meta:
        model= User
        fields = {"username","first_name","last_name" ,"email", "password1", "password2"}