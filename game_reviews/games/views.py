
# region ==== Imports ========================================================/
import collections
from decimal import *
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.db.models import Sum
from django.contrib.auth import authenticate


from .models import Game, GenreTag, ThemeTag, MiscTag
from .forms import GameSortShowForms, GameFilterGenreForm
from reviews.models import Review
from users.models import UserCommentsScore
# endregion
# ============================================================================/


# region ==== Games List =====================================================/


def game_list_view(request, *args, **kwargs):
    sort_in = request.GET.get('sort', 'none')

    sort_out = '-release_date'
    if sort_in != 'none':
        sort_out = order_by(sort_in)
        print('order_by function triggered')

    print('Sort In: ' + str(sort_in))
    print('Sort out: ' + str(sort_out))
    games = Game.objects.all().order_by(sort_out)
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

    if sort_in == 'Order by date (Desc)':
        return 'release_date'
    elif sort_in == 'Order by date (Asc)':
        return '-release_date'
    elif sort_in == 'Order by score (Desc)':
        return 'avg_score'
    elif sort_in == 'Order by score (Asc)':
        return '-avg_score'
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


# endregion
# ============================================================================/


# region ==== Game Details ===================================================/
def game_details_view(request):
    gameid = request.GET.get('gameid', 'none')
    if gameid != 'none':
        game = Game.objects.filter(id=gameid)
        if request.user.is_authenticated:
            userid = request.user.id
            session_user_comment_scores = UserCommentsScore.objects.filter(
                game__id=gameid, user__id=userid)
            all_user_comment_scores = UserCommentsScore.objects.filter(
                game__id=gameid).exclude(user__id=userid)
        else:
            session_user_comment_scores = ""
            all_user_comment_scores = UserCommentsScore.objects.filter(
                game__id=gameid)
        context = {
            'this_game': game,
            'all_user_comment_scores': all_user_comment_scores,
            'session_user_comment_scores': session_user_comment_scores,
        }
        return render(request, "game_details.html", context)
    return redirect(game_list_view)

# endregion
# ============================================================================/
