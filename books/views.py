from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Book

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q


# Objetivo: listar todos os livros presentes no Banco de Dados
class BookListView(ListView): 
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/book_list.html'


# Objetivo: retirar informações sobre algum livro específico selecionado pelo usuário
class BookDetailView(LoginRequiredMixin, DetailView): 
    model = Book
    context_object_name = 'book'
    template_name = 'books/book_detail.html'
    login_url = 'account_login'
    permission_required = 'books.special_status'


# Objetivo: realizar pesquisas e exibir resultados
class SearchResultsListView(ListView): 
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/search_results.html'

    def get_queryset(self): 
        query = self.request.GET.get('q')
        return Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))

# Objetivo: permitir usuário adicionar livros novos
class NewBookAdd(LoginRequiredMixin, CreateView):
    login_url = 'account_login'
    model = Book
    template_name = 'books/book_add.html'
    fields = ['title','author', 'cover']