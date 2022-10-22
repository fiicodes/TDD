from django.http import HttpResponse
from django.shortcuts import render
from django.http import response

# Create your views here.
def home_page(request):
  return HttpResponse('<html><title>To-Do Lists</title></html>')