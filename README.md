# Сайт для управления личными заметками

Добавляй и изменяй заметки под своим аккаунтом.

Используй **api** для своих целей

## Фишки

- авторизация
- заметки
- категории
- БД
- api

### Стек

- Django 4.2
- DRF
- Postgres
- Redis (кэш заметок и категорий)
- Pytest
- Celery

### Доп. библиотеки
- pytils (slugify)
- python-dotenv

## Запуск
```python
python manage.py runserver
```
## Тесты
Лежат в tests/

Запуск из todo_app/
```python
pytest
```