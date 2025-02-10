from django.forms import models
from django.forms.widgets import Select, TextInput

from .models import Note, Category


class AddNoteForm(models.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'text', 'category', 'color']
        widgets = {
            'category': Select(attrs={'class': 'input', }),
            'color': Select(attrs={'class': 'input', }),
        }

    def __init__(self, *args, **kwargs):
        super(AddNoteForm, self).__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Без категории'
        self.fields['color'].choices = Note.Color.choices


class AddCategoryForm(models.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': TextInput(attrs={'class': 'input', })
        }
