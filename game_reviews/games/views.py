from django.shortcuts import render
from django.http import HttpResponse


from .models import Game
from reviews.models import Review

# Create your views here.


def game_list_view(request):
    games = Game.objects.all()
    reviews = Review.objects.all()
    reviews_array = []
    for rev in reviews:
        reviews_array.append(rev)
    print(reviews_array)
    print(reviews)
    context = {
        'games': games,
        'reviews': reviews_array
    }

    return render(request, "games_list.html", context)
