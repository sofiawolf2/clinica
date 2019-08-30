from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from exames.models import Exame

# Create your views here.

# class ExameCreateView(LoginRequiredMixin, CreateView):
#     model = Exame
#     form_class = ExameCreateForm
#     # context_object_name = 'addPosts'
#     template_name = 'exames/addexames.html'
#     success_url = reverse_lazy('exames:detalhes_exames')

