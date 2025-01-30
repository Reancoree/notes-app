from django.shortcuts import render
from .models import Note


def index(request):
    notes = Note.public.all()
    empty = not Note.public.exists()
    data = {
        'notes': notes,
        'empty': empty,
    }

    return render(request, 'note/index.html', context=data)
