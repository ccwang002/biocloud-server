from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class ExampleForm(forms.Form):
    like_website = forms.TypedChoiceField(
        label="Do you like this website?",
        choices=((1, "Yes"), (0, "No")),
        coerce=lambda x: bool(int(x)),
        widget=forms.RadioSelect,
        initial='1',
        required=True,
    )

    favorite_food = forms.CharField(
        label="What is your favorite food?",
        max_length=80,
        required=True,
    )

    favorite_color = forms.CharField(
        label="What is your favorite color?",
        max_length=80,
        required=True,
    )

    favorite_number = forms.IntegerField(
        label="Favorite number",
        required=False,
    )

    notes = forms.CharField(
        label="Additional notes or feedback",
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super(ExampleForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'example_form'

        submit = Submit('submit', 'Submit')
        submit.field_classes = 'ui button'
        self.helper.add_input(submit)

    def clean_favorite_number(self):
        data = self.cleaned_data['favorite_number']
        if data and data <= 0:
            raise forms.ValidationError(
                'Invalid value: %(value)s, should be >= 1',
                code='neg_fav_number',
                params={'value': data},
            )
        return data

    def clean_favorite_color(self):
        data = self.cleaned_data['favorite_color']
        if data and not data == 'Red':
            raise forms.ValidationError('Should always be Red.')
        return data
