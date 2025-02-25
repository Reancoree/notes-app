from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.core.cache import cache
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from .forms import AddNoteForm, AddCategoryForm
from .models import Note, Category
from .utils import DataMixin


class IndexPage(DataMixin, ListView):
    template_name = 'note/index.html'
    title = 'Главная'
    h1 = 'Заметки'

    def get_queryset(self):
        user = self.request.user
        cat_id = self.request.GET.get('cat_id')

        cache_key = f'user_{user.id}_notes_cat_{cat_id or "all"}'

        cached_queryset = cache.get(cache_key)
        if cached_queryset is not None:
            return cached_queryset

        try:
            if cat_id:
                queryset = Note.public.for_user(user, category_id=cat_id)
            else:
                queryset = Note.public.for_user(user)
        except (Category.DoesNotExist, ValueError):
            queryset = Note.public.for_user(user)

        cache.set(cache_key, queryset, timeout=300)  # Кэшируем на 5 минут
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.for_user(self.request.user)
        return context


class AddNotePage(DataMixin, CreateView):
    model = Note
    form_class = AddNoteForm
    template_name = 'note/add_note.html'
    success_url = reverse_lazy('index')
    title = 'Новая заметка'
    h1 = 'Добавить заметку'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UpdateNotePage(DataMixin, UpdateView):
    model = Note
    template_name = 'note/change_note.html'
    form_class = AddNoteForm
    success_url = reverse_lazy('index')
    context_object_name = 'note'
    title = 'Изменение заметки'
    h1 = 'Изменить заметку'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.form_class.Meta.fields += ['color']
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

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.user != self.request.user:
            raise PermissionDenied("У вас нет прав для удаления этой заметки.")
        return obj


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
        user = self.request.user
        cache_key = f'user_{user.id}_categories'

        cached_categories = cache.get(cache_key)
        if cached_categories is not None:
            return cached_categories

        categories = Category.objects.for_user(user)
        cache.set(cache_key, categories, timeout=300)
        return categories


class AddCategoryPage(DataMixin, CreateView):
    model = Category
    template_name = 'note/add_category.html'
    success_url = reverse_lazy('category')
    form_class = AddCategoryForm
    title = 'Новая категория'
    h1 = 'Добавить категорию'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


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

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.user != self.request.user:
            raise PermissionDenied("У вас нет прав для удаления этой категории.")
        return obj
