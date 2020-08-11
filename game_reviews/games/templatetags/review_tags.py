from django import template
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from reviews.models import Review
from games.models import Game

register = template.Library()


@register.simple_tag
def review_tags(n, _game_id,  *args, **kwargs):
    game_id = _game_id
    print(game)
    reviews = Review.objects.filter(game__id=game_id)
    return reviews[0:n]


@register.simple_tag
def review_tags(n, _pk,  *args, **kwargs):
    pk = _pk
    print(game)
    reviews = Review.objects.filter(game__id=game_id)
    return reviews[0:n]
