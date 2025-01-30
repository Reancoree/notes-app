from django.db import models
from pytils.translit import slugify


class Note(models.Model):
    class Color(models.TextChoices):
        DEFAULT = 'default', 'Обычный'
        RED = 'red', 'Красный'
        BlUE = 'blue', 'Голубой'
        YELLOW = 'yellow', 'Желтый'
        GREEN = 'green', 'Зеленый'

    title = models.CharField(
        max_length=255, blank=False, verbose_name='Название')
    text = models.TextField(blank=True, verbose_name='Текст')
    time_create = models.DateTimeField(
        auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(
        auto_now=True, verbose_name='Время обновления')
    color = models.CharField(max_length=15, choices=Color.choices,
                             blank=True, default=Color.DEFAULT, verbose_name='Цвет заметки')
    is_deleted = models.BooleanField(
        blank=False, default=False, verbose_name='В корзине')
    category = models.ForeignKey(
        'Category', on_delete=models.PROTECT, null=True, blank=True, verbose_name='Категория')

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=50, blank=False,
                            verbose_name='Название')
    slug = models.SlugField(blank=False, verbose_name='Slug')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
