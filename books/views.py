from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Book, Review, Category

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy

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

    def get_context_data(self,*args, **kwargs):
        context = super(BookDetailView, self).get_context_data(*args,**kwargs)
        context['user_name'] = self.request.user
        return context

# Objetivo: realizar pesquisas e exibir resultados
class SearchResultsListView(ListView): 
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/search_results.html'

    def get_queryset(self): 
        query = self.request.GET.get('q')
        return Book.objects.filter(
            Q(title__icontains=query)|Q(texto__icontains=query)
        )

# Objetivo: permitir que o usuário adicionar livros novos
class NewBookAdd(LoginRequiredMixin, CreateView):
    login_url = 'account_login'
    model = Book
    template_name = 'books/book_add.html'
    fields = ['title', 'category','texto', 'cover']
    success_url = reverse_lazy('book_list')

    def form_valid(self, form):
        user = self.request.user
        form.instance.author = user
        return super(NewBookAdd, self).form_valid(form)

# Objetivo: permitir que o usuário adicione comentários a postagens específicas
class NewComment(LoginRequiredMixin, CreateView):
    login_url = 'account_login'
    model = Review
    template_name = 'books/book_comment.html'
    fields = ['review']

    def form_valid(self, form):
        user = self.request.user
        form.instance.book = Book.objects.get(id=self.kwargs['pk'])
        form.instance.author = self.request.user
        return super(NewComment, self).form_valid(form)

    def get_success_url(self):
          book_id=self.kwargs['pk']
          return reverse_lazy('book_detail', kwargs={'pk': book_id})

# Objetivo: permitir que o usuário edite comentários a postagens específicas
class EditComment(LoginRequiredMixin, UpdateView):
    login_url = 'account_login'
    model = Review
    template_name = 'books/book_editComment.html'
    fields = ['review']
    
    def get_context_data(self,*args, **kwargs):
        context = super(EditComment, self).get_context_data(*args,**kwargs)
        context['user_pk'] = self.kwargs['pk']
        return context
    def get_success_url(self):
          book_id=self.kwargs['id_dados']
          return reverse_lazy('book_detail', kwargs={'pk': book_id})

# Objetivo: permitir que o usuário delete comentários específicos
class DeleteComment(LoginRequiredMixin, DeleteView):
    login_url = 'account_login'
    model = Review
    template_name = 'books/delete_comment.html'

    def get_success_url(self):
          book_id=self.kwargs['id_dados']
          return reverse_lazy('book_detail', kwargs={'pk': book_id})

