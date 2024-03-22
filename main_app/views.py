from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import *

def main(request):
    template = loader.get_template("main.html")
    return HttpResponse(template.render())    
