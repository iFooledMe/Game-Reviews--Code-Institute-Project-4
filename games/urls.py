from django.urls import path
from .views import (
	game_list_view,
	reset_filters,
	game_details_view,
	hide_top_info,
	add_comment,
	edit_comment,
	delete_comment	
)

urlpatterns = [
    path('', game_list_view, name='game_list'),
    path('reset_filters/', reset_filters, name='reset_filters'),
    path('game_details/<int:game_id>/',game_details_view, name='game_details'),
    path('game_details/hide_top_info/', hide_top_info, name='hide_top_info'),
    path('game_details/add_comment/', add_comment, name='add_comment'),
    path('game_details/edit_comment/', edit_comment, name='edit_comment'),
    path('game_details/delete_comment/', delete_comment, name='delete_comment'),
]