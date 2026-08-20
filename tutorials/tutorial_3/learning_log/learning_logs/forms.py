"""Allowing users to enter data."""
from django import forms

from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    """Inherits from forms.ModelForm."""
    class Meta:
        """Tells Django which model to base the form on."""
        model = Topic
        fields = ['text']
        labels = {'text': ''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
