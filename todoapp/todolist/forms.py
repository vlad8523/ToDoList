from django import forms
from django.forms import ModelForm

from .models import *


class addTaskForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['importance'].empty_label = 'Choose importance'

    class Meta:
        model = Task
        fields = ['title', 'description', 'importance']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-title'}),
            'description': forms.Textarea(attrs={'class': 'form-desc'})
        }


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-title'}),
            'description': forms.Textarea(attrs={'class': 'form-desc'})
        }
