from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from exames.models import Exame
from exames.forms import ExameCreateForm
from django.urls import reverse_lazy

# Create your views here.

class ExameCreateView(LoginRequiredMixin, CreateView):
    model = Exame
    form_class = ExameCreateForm
    template_name = 'exames/addexames.html'
    success_url = reverse_lazy('exames:list_exames')
    # context_object_name = 'addPosts'

# class ExameListView(LoginRequiredMixin, ListView):
#     model = Exame
#     context_object_name = 'exames'
#     template_name = 'exames/list_exames.html'
#     ordering = ['-created_at',]

# class ExameDetailView(generic.DetailView):
#     model = Exame
#     template_name = 'exames/detail_exames.html'
#     context_object_name = 'exames'

