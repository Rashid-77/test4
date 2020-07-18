from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'app/index.html')


def provider(request):
    return HttpResponse("<h4>Hello provider</h4>")


def buyer(request):
    return HttpResponse("<h4>Hello buyer</h4>")


def login(request):
    return render(request, 'app/login.html')