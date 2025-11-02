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

import logging
from django_redis import get_redis_connection

logger = logging.getLogger(__name__)

def get_redis_cache_metrics():
    """
    Retrieves Redis keyspace hit/miss metrics and calculates hit ratio.
    Returns a dictionary with hits, misses, and hit_ratio.
    """
    redis_conn = get_redis_connection("default")  # uses 'default' cache
    info = redis_conn.info()  # get Redis server info

    hits = info.get("keyspace_hits", 0)
    misses = info.get("keyspace_misses", 0)
    total = hits + misses
    hit_ratio = hits / total if total > 0 else 0.0

    metrics = {
        "keyspace_hits": hits,
        "keyspace_misses": misses,
        "hit_ratio": hit_ratio,
    }

    logger.info(f"Redis cache metrics: {metrics}")
    return metrics
