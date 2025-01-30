# Generated by Django 4.2 on 2025-01-30 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('text', models.TextField(blank=True, verbose_name='Текст')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Время обновления')),
                ('color', models.CharField(blank=True, choices=[('default', 'Обычный'), ('red', 'Красный'), ('blue', 'Голубой'), ('yellow', 'Желтый'), ('green', 'Зеленый')], default='default', max_length=15, verbose_name='Цвет заметки')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='В корзине')),
            ],
        ),
    ]
