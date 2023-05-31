from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
import random

# Create your views here.
def home(request):
    return HttpResponse('<h1>Hello World, my first django project</h1>')
def passgen(request):
    char=list('abcdefghijklmnopqrstuvwxyz')
    password=""
    for x in range(10):
        password+= random.choice(char)
    pas={'password':password}
    return JsonResponse(pas)