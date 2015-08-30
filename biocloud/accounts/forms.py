from django import forms
from crispy_forms.helper import FormHelper
from django.contrib.auth.forms import UserCreationForm as _UserCreationForm

from django.contrib.auth.models import User
from .models import Account


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('description', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.disable_csrf = True

class UserCreationForm(_UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.disable_csrf = True
