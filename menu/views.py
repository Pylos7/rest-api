from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .serializers import ItemSerializer
from .models import Item

# Create your views here.

def item_list(request):
    # QueryObj => Python list[dicts]
    items = Item.objects.all()
    item_list = []
    for item in items:
        item_list.append({
            "name": item.name,
            "price": item.price,
            "description": item.description,
        })
    return JsonResponse({"menu_items": item_list})

# Serialization = changing data types into other datatypes

def item_list_serialized(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return JsonResponse(serializer.data, safe=False)