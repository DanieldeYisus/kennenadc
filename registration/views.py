from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import ClienteForm
from django import forms
# Create your views here.

class RegistroView(CreateView):
    form_class = ClienteForm
    template_name = 'registration/registro.html'

    def get_success_url(self):
        return reverse_lazy('login') + '?register'
    
        

    