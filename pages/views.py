from django.shortcuts import render
from django.views.generic import TemplateView 
from books.models import Book, Category

from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
# Create your views here.



class HomePageView(TemplateView): 
    template_name = 'home.html'




#Páginas relacionadas ao fórum

# Objetivo: listar , na forma de um fórum, as informações presentes no banco de dados
class ForumView(ListView):
    model = Category
    template_name = 'books/forum_book.html'

    def get_context_data(self,*args, **kwargs):
        context = super(ForumView, self).get_context_data(*args,**kwargs)
        context['category'] = Category.objects.order_by('title')
        return context