from django.core.cache import cache

from config import settings


def cash_category(categories):
    if settings.CACHE_ENABLE:
        key = f'subject_list'
        category_list = cache.get(key)
        if category_list is None:
            category_list = categories
            cache.set(key, category_list)
    else:
        category_list = categories

    cash_categories = category_list
    return cash_categories
