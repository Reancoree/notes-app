from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from .utils import DataMixin
from .models import Note, Category


class IndexPage(DataMixin, ListView):
    template_name = 'note/index.html'
    title = 'Главная'
    h1 = 'Заметки'

    def get_queryset(self):
        cat_id = self.request.GET.get('cat_id')

        if cat_id:
            try:
                cat = Category.objects.get(pk=cat_id)
                return cat.notes.filter(is_deleted=False)
            except (Category.DoesNotExist, ValueError):
                return Note.public.all()

        return Note.public.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


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
    context_object_name = 'note'
    title = 'Изменение заметки'
    h1 = 'Изменить заметку'

    fields = ['title', 'text', 'color', 'category']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.get_object().is_deleted:
            context['title'] = 'Заметка в корзине'
            context['h1'] = 'Заметка в корзине'
            return context
        return context

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()

        if request.GET.get('trash'):
            self.object.is_deleted = True
            self.object.save()
            return HttpResponseRedirect(self.success_url)

        if request.GET.get('restore'):
            self.object.is_deleted = False
            self.object.save()
            return HttpResponseRedirect(self.success_url)

        return super().get(request, *args, **kwargs)


class DeleteNotePage(DataMixin, DeleteView):
    model = Note
    template_name = 'note/delete_note.html'
    success_url = reverse_lazy('trash')
    title = 'Удаление заметки'
    h1 = title


class TrashNotePage(DataMixin, ListView):
    model = Note
    template_name = 'note/trash.html'

    title = 'Корзина'
    h1 = title

    def get_queryset(self):
        return Note.objects.filter(is_deleted=True)


class CategoryPage(DataMixin, ListView):
    model = Category
    template_name = 'note/category.html'
    context_object_name = 'categories'

    title = 'Категории'
    h1 = title

    def get_queryset(self):
        return Category.objects.all()


class AddCategoryPage(DataMixin, CreateView):
    model = Category
    template_name = 'note/add_category.html'
    success_url = reverse_lazy('category')
    title = 'Новая категория'
    h1 = 'Добавить категорию'

    fields = ['name']


class UpdateCategoryPage(DataMixin, UpdateView):
    model = Category
    template_name = 'note/update_category.html'

    title = 'Редактирование категории'
    h1 = title
    context_object_name = 'category'

    fields = ['name']


class DeleteCategoryPage(DataMixin, DeleteView):
    model = Category
    template_name = 'note/delete_category.html'
    success_url = reverse_lazy('category')
    title = 'Удаление категории'
    h1 = title
