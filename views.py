# views.py
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import State

class StateListView(ListView):
    model = State
    template_name = 'state_list.html'

class StateDetailView(DetailView):
    model = State
    template_name = 'state_detail.html'

class StateCreateView(CreateView):
    model = State
    template_name = 'state_form.html'
    fields = ['name', 'population', 'language', 'capital']
    success_url = reverse_lazy('state_list')

class StateUpdateView(UpdateView):
    model = State
    template_name = 'state_form.html'
    fields = ['name', 'population', 'language', 'capital']
    success_url = reverse_lazy('state_list')

class StateDeleteView(DeleteView):
    model = State
    template_name = 'state_confirm_delete.html'
    success_url = reverse_lazy('state_list')
