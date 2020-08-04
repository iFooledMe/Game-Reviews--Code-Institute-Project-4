from django.shortcuts import render
from django.http import HttpResponse
from .models import Game

# Create your views here.
def game_list_view(request):
	game = Game.objects.get(id=1)
	context = {
		'game' : game
	}

	return render(request, "games_list.html", context)