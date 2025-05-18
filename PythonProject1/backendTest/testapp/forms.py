### forms.py (в testapp)
from django import forms
from .models import Question

class TestForm(forms.Form):
    def __init__(self, *args, **kwargs):
        questions = kwargs.pop('questions')
        super().__init__(*args, **kwargs)
        for question in questions:
            self.fields[f"question_{question.id}"] = forms.CharField(
                label=question.text,
                max_length=255
            )
