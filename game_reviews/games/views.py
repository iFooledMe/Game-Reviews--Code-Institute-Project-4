from django.shortcuts import render
from django.http import HttpResponse
from .models import Game

# Create your views here.


def game_list_view(request):
    games = Game.objects.all()
    context = {
        'games': games,
    }

    return render(request, "games_list.html", context)
