from django.shortcuts import render
from django.http import HttpResponse

def start(request):
  return render(request,'test.html')


def found(request):
  return render(request,'404.html')
