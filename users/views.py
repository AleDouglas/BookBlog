from django.shortcuts import render

from django.views.generic import UpdateView, ListView, DetailView
from .models import CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
# Create your views here.


# Objetivo: Editar o profile do usuário, podendo adicionar: biografia, ícone de avatar, entre outras funções disponíveis.
class EditProfile(LoginRequiredMixin, UpdateView):
    login_url = 'account_login'
    model = CustomUser
    template_name = 'account/edit_profile.html'
    fields = ['username','first_name','last_name','perfilIMG','bio','birth_date']

    def get_context_data(self,*args, **kwargs):
        context = super(EditProfile, self).get_context_data(*args,**kwargs)
        context['user_pk'] = self.kwargs['pk']
        return context

    def get_success_url(self):
          id_user=self.kwargs['pk']
          return reverse_lazy('profile', kwargs={'pk': id_user})

# Objetivo: Exibir o Profile do Usuário
class ViewProfile(LoginRequiredMixin, DetailView):
    login_url = 'account_login'
    model = CustomUser
    context_object_name = 'user_dados'
    template_name = 'account/profile_page.html'

    def get_context_data(self,*args, **kwargs):
        context = super(ViewProfile, self).get_context_data(*args,**kwargs)
        context['user_pk'] = self.kwargs['pk']
        return context