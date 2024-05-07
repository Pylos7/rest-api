from django.shortcuts import render, HttpResponse

from .models import Item

# Create your views here.

def item_list(request):
    return HttpResponse("Hello World")