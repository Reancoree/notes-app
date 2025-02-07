from django.shortcuts import render
from django.views.generic import ListView

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
