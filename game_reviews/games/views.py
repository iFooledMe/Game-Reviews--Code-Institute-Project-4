from django.shortcuts import render
from django.http import HttpResponse
from .models import Game

# Create your views here.
def game_list_view(*args, **kwargs):
	return HttpResponse("<h3>game list view</h3>")