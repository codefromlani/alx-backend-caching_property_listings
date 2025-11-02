from django.core.cache import cache
from .models import Property

def get_all_properties():
    """
    Returns all Property objects, cached in Redis for 1 hour.
    """
    properties = cache.get('all_properties')
    if properties is None:
        properties = list(Property.objects.all())
        cache.set('all_properties', properties, 3600)  # 1 hour
    return properties
