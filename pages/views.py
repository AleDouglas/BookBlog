from django.shortcuts import render
from django.views.generic import TemplateView 
from books.models import Book, Category

from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
# Create your views here.



class HomePageView(TemplateView): 
    template_name = 'home.html'




#Páginas relacionadas ao fórum

# Objetivo: listar , na forma de um fórum, as informações presentes no banco de dados
class ForumView(ListView):
    model = Category
    template_name = 'forum/forum_book.html'

    def get_context_data(self,*args, **kwargs):
        context = super(ForumView, self).get_context_data(*args,**kwargs)
        context['category'] = Category.objects.order_by('position')
        return context


# Objetivo: retirar informações sobre algum tópico específico selecionado pelo usuário
class ForumDetailView(LoginRequiredMixin, DetailView): 
    model = Book
    context_object_name = 'book'
    template_name = 'forum/forum_detail.html'
    login_url = 'account_login'

    def get_context_data(self,*args, **kwargs):
        context = super(BookDetailView, self).get_context_data(*args,**kwargs)
        context['user_name'] = self.request.user
        return context