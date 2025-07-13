from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from django.core import serializers
from .models import Property
from .utils import get_all_properties

@cache_page(60 * 15)  # Cache for 15 minutes
def property_list(request):
    """
    View to return all properties with caching applied.
    This view is cached for 15 minutes using @cache_page decorator.
    """
    properties = get_all_properties()
    
    # Convert queryset to list of dictionaries for JSON response
    properties_data = []
    for property in properties:
        properties_data.append({
            'id': property.id,
            'title': property.title,
            'description': property.description,
            'price': str(property.price),
            'location': property.location,
            'created_at': property.created_at.isoformat()
        })
    
    return JsonResponse({
        'properties': properties_data,
        'count': len(properties_data)
    })

def property_detail(request, property_id):
    """
    View to return a single property by ID.
    """
    try:
        property = Property.objects.get(id=property_id)
        property_data = {
            'id': property.id,
            'title': property.title,
            'description': property.description,
            'price': str(property.price),
            'location': property.location,
            'created_at': property.created_at.isoformat()
        }
        return JsonResponse({'property': property_data})
    except Property.DoesNotExist:
        return JsonResponse({'error': 'Property not found'}, status=404)