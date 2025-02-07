from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from .utils import DataMixin
from .models import Note


class IndexPage(DataMixin, ListView):
    template_name = 'note/index.html'
    context_object_name = 'notes'
    title = 'Главная'
    h1 = 'Заметки'

    def get_queryset(self):
        return Note.public.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context)


class AddNotePage(CreateView):
    template_name = 'note/add_note.html'
    model = Note
    success_url = reverse_lazy('index')
    
    fields = ['title', 'text', 'category']
