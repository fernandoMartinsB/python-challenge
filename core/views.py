from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render 

""" Long tearm template request """
# def index(request):
#     return HttpResponse(loader.get_template('core/index.html').render({},request))

""" Short tearm template request"""
def index(request):
    return render(request, 'core/index.html', {})