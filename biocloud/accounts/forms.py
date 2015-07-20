from django import forms
from django.contrib.auth.forms import UserCreationForm as _UserCreationForm

from django.contrib.auth.models import User
from .models import Account


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('description', )


class UserCreationForm(_UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

