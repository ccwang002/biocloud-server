from django import forms
# from django.forms.models import inlineformset_factory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Sample


class UploadSampleForm(forms.ModelForm):

    class Meta:
        model = Sample
        fields = ('name', 'sample_file',)
