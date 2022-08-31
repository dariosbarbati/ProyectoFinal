from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render

def principal (request):
    return render(request , "index.html", context={})
