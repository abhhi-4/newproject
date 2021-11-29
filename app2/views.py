from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def fn1(re):
    return HttpResponse("hai")
def fn2(req):
    return render(req,'abhi.html')
def fn3(req):
    return render(req,'images.html')