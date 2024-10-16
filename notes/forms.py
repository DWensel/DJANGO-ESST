from django import forms
from django.core.exceptions import ValidationError
from .models import Notes

# This can quickly be setup by just typing modelforms and selection the option that appears
class NotesForm(forms.ModelForm):
    # Meta data from model. Here we specify the model and the fields we want to appear on the form
    class Meta:
        model = Notes
        fields = ("title","text")

    def clean_title(self):
        title = self.cleaned_data['title'] # Clean data is returned by the form, here it will be the same value the user passed
        if 'Django' not in title:
            raise ValidationError('We only accept notes about Django!')
        return title