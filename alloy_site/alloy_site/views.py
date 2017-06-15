from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('alloy_site/index.html')
    context = {} # doing nothing dynamic now
    
    
    return HttpResponse(template.render(context, request))
            
