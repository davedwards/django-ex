from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    resume = None
    with open('resume/David_Edwards_Resume.html', 'r') as f:
        resume = f.read()
    if resume:
        return HttpResponse(resume)
