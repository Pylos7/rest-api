from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import Item

# Create your views here.

def item_list(request):
    items = Item.objects.all()
    item_list = []
    for item in items:
        item_list.append({
            "name": item.name,
            "price": item.price,
            "description": item.description,
        })
    return JsonResponse({"menu_items": item_list})
