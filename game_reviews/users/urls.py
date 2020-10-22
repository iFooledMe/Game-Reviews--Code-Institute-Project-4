from django.urls import path
from .views import (
	user_profile_view,
	user_profile_edit,
	change_avatar,
	pay_thankyou_view,
)

urlpatterns = [
	path('userprofile/', user_profile_view, name='userprofile'),
	path('userprofile_edit//', user_profile_edit, name='userprofile_edit'),
	path('changeavatar/<int:avatar_id>/',change_avatar, name='change_avatar'),
	path('pay_thankyou/', pay_thankyou_view, name='pay_thankyou')
]

