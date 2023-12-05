# nomapp/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import CustomUser




from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from authentificationn.models import CustomUser  # Update the import statement

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser  # Use the CustomUser model
        fields = ['email', 'password1', 'password2']

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser 
        fields = ['email', 'password'] # Use the CustomUser model


  # authentificationn/forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomAuthenticationForm(AuthenticationForm):
    # Add any customizations you need here, if necessary
    pass

       
