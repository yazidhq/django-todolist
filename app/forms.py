from django import forms
from .models import Todolist


class ItemForm(forms.ModelForm):
    item = forms.CharField(
        label="",
        required=False,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter a task here [ENTER]'
            }
        ),
    )

    class Meta:
        model = Todolist
        fields = ('item', )
