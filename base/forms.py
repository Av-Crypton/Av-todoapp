from django import forms
from django.forms import ModelForm
from .models import Task

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'

    def clean(self):
        super(TaskForm, self).clean()

        title = self.cleaned_data.get('title')
        time = self.cleaned_data.get('time')

        return self.cleaned_data