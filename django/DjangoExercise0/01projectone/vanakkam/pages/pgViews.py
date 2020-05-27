from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def samplePage(request):
    return HttpResponse("This is sample page!")