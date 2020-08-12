import collections
from decimal import *
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Sum


from .models import Game
from reviews.models import Review

# Create your views here.


def game_list_view(request):
    games = Game.objects.all()
    game_scores = collections.defaultdict(list)
    for game in games:
        scores_sum = Review.objects.filter(
            game__id=game.id).aggregate(Sum('score'))
        scores_max = Review.objects.filter(
            game__id=game.id).aggregate(Sum('max_score'))

        sum = scores_sum.get('score__sum')
        max = scores_max.get('max_score__sum')
        avg_score = round((sum / max) * 100, 0)
        game_scores[game.id].append(avg_score)
    print(game_scores)

    context = {
        'games': games,
        'game_scores': game_scores
    }

    return render(request, "games_list.html", context)
