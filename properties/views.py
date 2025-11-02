from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from .utils import get_all_properties

# Cache the full response for 15 minutes
@cache_page(60 * 15)
def property_list(request):
    properties = get_all_properties()  # use the low-level cache
    data = [
        {
            "id": p.id,
            "title": p.title,
            "description": p.description,
            "price": str(p.price),
            "location": p.location,
            "created_at": p.created_at,
        }
        for p in properties
    ]
    return JsonResponse({'data': data})
