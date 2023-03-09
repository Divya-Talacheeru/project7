from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def DSP(request):
    return HttpResponse('<h1>this is DSP</h1>')
