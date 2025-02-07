from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView

from .utils import DataMixin
from .models import Note


class IndexPage(DataMixin, ListView):
    template_name = 'note/index.html'
    context_object_name = 'notes'
    title = 'Главная'
    h1 = 'Заметки'

    def get_queryset(self):
        return Note.public.all()


class AddNotePage(DataMixin, CreateView):
    model = Note
    template_name = 'note/add_note.html'
    success_url = reverse_lazy('index')
    title = 'Новая заметка'
    h1 = 'Добавить заметку'

    fields = ['title', 'text', 'category']


class UpdateNotePage(DataMixin, UpdateView):
    model = Note
    template_name = 'note/change_note.html'
    success_url = reverse_lazy('index')
    title = 'Изменение заметки'
    h1 = 'Изменить заметку'
    
    fields = ['title', 'text', 'color', 'category']
    
    
