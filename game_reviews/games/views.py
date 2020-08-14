import collections
from decimal import *
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.db.models import Sum


from .models import Game, GenreTag, ThemeTag, MiscTag
from .forms import GameSortShowForms, GameFilterGenreForm
from reviews.models import Review

# Create your views here.


def game_list_view(request):
    if request.method == "POST":
        sort_in = request.POST.get('sort')
        sort_out = order_by(sort_in)
        print(sort_out)
        test = '-release_date'
        return HttpResponseRedirect(request.path_info)
    games = Game.objects.all().order_by('-release_date')
    update_avg_score(games)

    search_show_form = GameSortShowForms()
    genre_tags_filter = GameFilterGenreForm()

    context = {
        'games': games,
        'search_show_form': search_show_form,
        'genre_tags_filter': genre_tags_filter,
    }

    return render(request, "games_list.html", context)


def order_by(sort_in):
    if sort_in == 'Sort by date (Desc)':
        return 'release_date'
    elif sort_in == 'Sort by date (Asc)':
        return '-release_date'
    else:
        return 'release_date'


def update_avg_score(games):
    # Get review scores (for each game), calculate avg and update avg_score field in Game Object
    for game in games:
        scores_sum = Review.objects.filter(
            game__id=game.id).aggregate(Sum('score'))
        scores_max = Review.objects.filter(
            game__id=game.id).aggregate(Sum('max_score'))
        sum = scores_sum.get('score__sum')
        max = scores_max.get('max_score__sum')
        avg_score = round((sum / max) * 100, 0)
        Game.objects.filter(pk=game.id).update(avg_score=avg_score)
