from django.shortcuts import render
from django.views.generic import TemplateView # new

# Create your views here.



class HomePageView(TemplateView): # new
    template_name = 'home.html'
