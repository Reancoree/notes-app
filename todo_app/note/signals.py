from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache

from note.models import Category, Note


@receiver([post_save, post_delete], sender=Category)
def invalidate_category_cache(sender, instance, **kwargs):
    cache_key = f'user_{instance.user_id}_categories'
    cache.delete(cache_key)


@receiver([post_save, post_delete], sender=Note)
def invalidate_notes_cache(sender, instance, **kwargs):
    cache_key_all = f'user_{instance.user_id}_notes_cat_all'
    cache_key_id = f'user_{instance.user_id}_notes_cat_{instance.category_id}'
    cache.delete(cache_key_all)
    cache.delete(cache_key_id)
