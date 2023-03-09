from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def DSP(request):
    return HttpResponse('<h1><marquee>Dsp is the best singer</h1><marquee>')

