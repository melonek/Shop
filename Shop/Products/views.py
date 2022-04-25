from django.shortcuts import render
from django.http import HttpResponse
from .models import Products
# Create your views here.

def index(request):
    requestMethod = Products.objects.all()
    return HttpResponse(requestMethod)