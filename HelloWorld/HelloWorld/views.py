from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def page1(request):
    context = {'var1': 'hhh'}
    return render(request, 'page1.html',context)

def page2(request):
    return HttpResponse("HttpResponse is Hello world ! ")

# example1
# def index(request):
#     return HttpResponse("Hello world ! ")

# example2
# def index(request):
#     return HttpResponse("Hello world ! ")

# example3
# def index(request):
#     return HttpResponse("Hello world ! ")