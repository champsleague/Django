from django.shortcuts import render,HttpResponse
import random

# Create your views here.
def index(request):
    return HttpResponse('<h1>Random</h1>'+random.random)

def create(request):
    return HttpResponse('create')

def read(request,id):
    return HttpResponse('read'+id)