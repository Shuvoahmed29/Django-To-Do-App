from django import forms

from . models import Task

# Create a form for creating a new task.
class TodoForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'due_date','due_time')
        widgets = {
            "title":forms.TextInput(attrs={'class':'form-control'}),
            "description":forms.Textarea(attrs={'class':'form-control'}),
            "due_date": forms.DateInput(attrs={"type": "date",'class':'form-control'}),
            "due_time": forms.TimeInput(attrs={"type": "time",'class':'form-control'}),
        }