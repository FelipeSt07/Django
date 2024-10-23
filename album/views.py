from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from album.models import Team
from album.models import Player


def base_view(request):
    return render(request, 'base.html')  # Asegúrate de que la plantilla existe


# Create your views here.
class TeamListView(ListView):
    model = Team

class PlayerListView(ListView):
    model = Player

class TeamDetailView(DetailView):
    model = Team

class PlayerDetailView(DetailView):
    model = Player

class TeamCreate(CreateView):
    model = Team
    fields = '__all__'

class PlayerCreate(CreateView):
    model = Player
    fields = '__all__'

class TeamUpdate(UpdateView):
    model = Team
    fields = '__all__'

class PlayerUpdate(UpdateView):
    model = Player
    fields = '__all__'

class TeamDelete(DeleteView):
    model = Team
    success_url = reverse_lazy('team-list')

class PlayerDelete(DeleteView):
    model = Player
    success_url = reverse_lazy('player-list')