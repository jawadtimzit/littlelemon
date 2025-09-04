from django.shortcuts import render
from django.http import HttpResponse

def ping(request):
    return HttpResponse("Ping Restaurant")

def menu(request):
    return HttpResponse("Restaurant Menu...........")

def index(request):
    return render(request, 'index.html', {})
    

# Create your views here.