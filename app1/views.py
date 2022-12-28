from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def string_1(request):
    return HttpResponse('<h1> This is string_1 by using app1</h1>')

def string_2(request):
    return HttpResponse('<h2> This is string_2 by using app1</h2>')