from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from .utils import get_all_properties

@cache_page(60 * 15)
def property_list(request):
    # Using low-level cache helper from Task 2
    properties_list = get_all_properties()
    
    # Converting queryset objects to dictionary for JsonResponse as hinted by your error
    data = [
        {
            "title": p.title,
            "description": p.description,
            "price": str(p.price),
            "location": p.location
        } for p in properties_list
    ]
    
    return JsonResponse({"properties": data})
