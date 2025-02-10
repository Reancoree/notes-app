from django.forms import models
from django.forms.widgets import Select, Textarea, TextInput

from .models import Note, Category


class AddNoteForm(models.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'text', 'category']
        widgets = {
            'category': Select(attrs={'class': 'input', })
        }

    def __init__(self, *args, **kwargs):
        super(AddNoteForm, self).__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Без категории'


class AddCategoryForm(models.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': TextInput(attrs={'class': 'input', })
        }
