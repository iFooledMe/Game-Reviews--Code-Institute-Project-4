  
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include

from allauth.account.views import LoginView, SignupView, LogoutView
from games import views
from users.views import user_profile_view, pay_thankyou_view, user_profile_edit, change_avatar


urlpatterns = [
    path('', views.game_list_view, name='game_list'),
    path('reset_filters', views.reset_filters, name='reset_filters'),
    path('game_details/<int:game_id>',
         views.game_details_view, name='game_details'),
    path('hide_top_info', views.hide_top_info, name='hide_top_info'),
    path('add_comment', views.add_comment, name='add_comment'),
    path('edit_comment', views.edit_comment, name='edit_comment'),
    path('delete_comment', views.delete_comment, name='delete_comment'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('signup', SignupView.as_view(), name='signup'),
    path('userprofile', user_profile_view, name='userprofile'),
    path('userprofile_edit', user_profile_edit, name='userprofile_edit'),
    path('changeavatar/<int:avatar_id>',
         change_avatar, name='change_avatar'),
    path('pay_thankyou', pay_thankyou_view, name='pay_thankyou'),
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)