# region ==== Imports ========================================================/
import collections
from datetime import date, datetime, timedelta
from decimal import *

from django.contrib.auth import authenticate
from django.db.models import Avg, Sum
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from reviews.models import Review
from users.forms import EditCommentForm, NewCommentForm
from users.models import UserCommentsScore

from .forms import GameFilterGenreForm, GameSortShowForms
from .models import Game, GenreTag, MiscTag, ThemeTag
# endregion
# ============================================================================/

# region ==== Games List =====================================================/

# region --- MAIN FUNCTION ------------?--


def game_list_view(request, *args, **kwargs):
    genre_all = 'true'
    order_by = request.GET.get('sort', 'none')
    time_filter = request.GET.get('time', 'none')
    genre_all = request.GET.getlist('genre_all', 'none')
    genre_filter = request.GET.getlist('genre_filter', 'none')
    games = get_games(
        request,
        order_by,
        time_filter,
        genre_all,
        genre_filter)
    update_avg_score(games)
    search_show_form = GameSortShowForms()
    genre_tags_filter = GameFilterGenreForm()
    if 'hide_top_info' in request.session:
        hide_top_info = request.session.get('hide_top_info')
    else:
        hide_top_info = False

    context = {
        'games': games,
        'search_show_form': search_show_form,
        'genre_all': genre_all,
        'genre_tags_filter': genre_tags_filter,
        'hide_top_info': hide_top_info,
    }

    return render(request, "games_list.html", context)
# endregion ----
# -----------------------------------------

# region --- Get Games (filtered) ---------


def get_games(request, order_by_in, time_filter_in, genre_all, genre_filter_in):

    # Set date filter
    start_date = date.today() - \
        timedelta(days=get_time_filter_start_date(request, time_filter_in))
    games = Game.objects.filter(
        release_date__range=[start_date, date.today()])

    # Set genre filter
    games = set_genre_filter(request, games, genre_all, genre_filter_in)

    # Set sort order
    get_order_by(request, order_by_in)
    games = games.order_by(request.session.get('order_by_in'))

    return games

# region - Get date filter start date -


def get_time_filter_start_date(request, time_filter_in):
    if time_filter_in != 'none':
        request.session['time_filter_days'] = get_days(time_filter_in)
    if 'time_filter_days' not in request.session:
        request.session['time_filter_days'] = 36500
    return request.session.get('time_filter_days')


def get_days(time_filter_in):
    print(time_filter_in)
    if time_filter_in == 'Show last week':
        return 7
    elif time_filter_in == 'Show last month':
        return 30
    elif time_filter_in == 'Show last 3 months':
        return 90
    elif time_filter_in == 'Show last 6 months':
        return 180
    elif time_filter_in == 'Show last year':
        return 365
    elif time_filter_in == 'Show all time':
        return 36500
    else:
        return 36500
# endregion ----

# region - Get genre filter parameters -


def set_genre_filter(request, games, genre_all, genre_filter_in):
    if genre_filter_in == 'none' or genre_all == '1':
        return games
    else:
        request.session['genre_filter'] = genre_filter_in
        print('-------------------')
        print('Genre_filter_in:')
        print(genre_filter_in)
        print('-------------------')
        games_contain_doubles = games.filter(genre_tags__pk__in=genre_filter_in)

        list_of_ids = []
        for game in games:
            list_of_ids.append(game.id)
        print('List_of_ids:')
        print(list_of_ids)
        print('-------------------')

        no_doubles = [x for n, x in enumerate(list_of_ids) if x not in list_of_ids[:n]]
        print('no_doubles:')
        print(no_doubles)
        print('-------------------')


        games = games.filter(genre_tags__pk__in=list_of_ids)

        return games

# endregion ----

# region - Get sort parameter -


def get_order_by(request, order_by_in):
    if order_by_in != 'none':
        request.session['order_by_in'] = set_order_parameter(order_by_in)
    if 'order_by_in' not in request.session:
        request.session['order_by_in'] = '-release_date'


def set_order_parameter(order_by_in):
    if order_by_in == 'Order by date (Desc)':
        return 'release_date'
    elif order_by_in == 'Order by date (Asc)':
        return '-release_date'
    elif order_by_in == 'Order by score (Desc)':
        return 'avg_score'
    elif order_by_in == 'Order by score (Asc)':
        return '-avg_score'
    else:
        return '-release_date'
# endregion ----

# endregion ----
# -----------------------------------------

# region --- Reset filters ----------------


def reset_filters(request):
    if 'order_by_in' in request.session:
        del request.session['order_by_in']
    if 'time_filter_days' in request.session:
        del request.session['time_filter_days']
    if 'genre_filter' in request.session:
        del request.session['genre_filter']
    return redirect(game_list_view)
# endregion ----
# -----------------------------------------

# region --- Calculate Score --------------


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
# endregion ----
# ------------------------------------------

# endregion
# ============================================================================/

# region ==== Game Details ===================================================/

# region --- MAIN FUNCTION ----------------


def game_details_view(request, game_id):
    gameid = game_id
    if gameid != 'none':
        game = Game.objects.filter(id=gameid)
        update_avg_score(game)
        # Authenticated User
        if request.user.is_authenticated:
            userid = request.user.id
            all_user_comment_scores = UserCommentsScore.objects.filter(
                game__id=gameid).exclude(user__id=userid).order_by('-updated')
            try:
                session_user_comment_scores = UserCommentsScore.objects.filter(
                    game__id=gameid, user__id=userid)
                have_commented = True
                user_comment = UserCommentsScore.objects.get(
                    game__id=gameid, user__id=userid)
                edit_comment_form = EditCommentForm(instance=user_comment)
                context = {
                    'this_game': game,
                    'all_user_comment_scores': all_user_comment_scores,
                    'session_user_comment_scores': session_user_comment_scores,
                    'have_commented': have_commented,
                    'edit_comment_form': edit_comment_form,
                    'avg_user_score': calc_avg_user_score(game_id),
                }
                return render(request, "game_details.html", context)
            except:
                new_comment_form = NewCommentForm()
                have_commented = False
                context = {
                    'this_game': game,
                    'all_user_comment_scores': all_user_comment_scores,
                    'have_commented': have_commented,
                    'new_comment_form': new_comment_form,
                    'avg_user_score': calc_avg_user_score(game_id),
                }
                return render(request, "game_details.html", context)
        # Non Authenticated User
        all_user_comment_scores = UserCommentsScore.objects.filter(
            game__id=gameid).order_by('-updated')

        context = {
            'this_game': game,
            'all_user_comment_scores': all_user_comment_scores,
            'avg_user_score': calc_avg_user_score(game_id),
        }
        return render(request, "game_details.html", context)
    return redirect(game_list_view)
# endregion
# ------------------------------------------

# region --- Calculate Score --------------


def calc_avg_user_score(gameid):
    all_user_comment_scores_exlude_zero = UserCommentsScore.objects.filter(
        game__id=gameid).exclude(user_score__lte=0)
    if all_user_comment_scores_exlude_zero.count() > 0:
        aggregate_score = all_user_comment_scores_exlude_zero.aggregate(
            Avg('user_score'))
        return int(aggregate_score.get('user_score__avg') * 10)
    else:
        return 0
# endregion
# ------------------------------------------

# endregion
# ============================================================================/

# region ==== Hide Top Info  =================================================/


def hide_top_info(request):
    request.session['hide_top_info'] = True
    return redirect(game_list_view)
# endregion
# ============================================================================/

# region ==== Add comment ====================================================/


def add_comment(request):
    new_comment_form = NewCommentForm(request.POST)
    gameid = request.GET.get('gameid', 'none')
    userid = request.user.id
    session_user_comment_scores = UserCommentsScore.objects.filter(
        game__id=gameid, user__id=userid)
    if not session_user_comment_scores.exists():
        if new_comment_form.is_valid():
            game_instance = Game.objects.get(id=gameid)
            new_comment = new_comment_form.save(commit=False)
            new_comment.user = request.user
            new_comment.game = game_instance
            new_comment.save()
            return redirect('game_details', game_id=gameid)
    return redirect('game_details', game_id=gameid)

# endregion
# ============================================================================/

# region ==== Edit comment ===================================================/


def edit_comment(request):
    gameid = request.GET.get('gameid', 'none')
    userid = request.user.id
    comment_instance = UserCommentsScore.objects.get(
        game__id=gameid, user__id=userid)
    edit_comment_form = NewCommentForm(request.POST, instance=comment_instance)
    if edit_comment_form.is_valid():
        edit_comment_form.save()
        return redirect('game_details', game_id=gameid)
    return redirect('game_details', game_id=gameid)

# endregion
# ============================================================================/

# region ==== Delete comment =================================================/


def delete_comment(request):

    gameid = request.GET.get('gameid', 'none')
    userid = request.user.id
    UserCommentsScore.objects.get(
        game__id=gameid, user__id=userid).delete()
    # edit_comment_form = NewCommentForm(request.POST, instance=comment_instance)
    # if edit_comment_form.is_valid():
    # edit_comment = edit_comment_form.save(commit=False)
    # edit_comment.save()
    # return redirect('game_details', game_id=gameid)
    return redirect('game_details', game_id=gameid)

# endregion
# ============================================================================/
