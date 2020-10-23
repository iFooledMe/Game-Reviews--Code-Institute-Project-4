from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include, handler404, handler500

from allauth.account.views import LoginView, SignupView, LogoutView
from games.views import 	game_list_view, reset_filters, game_details_view, hide_top_info, add_comment, edit_comment,delete_comment
from users.views import user_profile_view, user_profile_edit, change_avatar, pay_thankyou_view
from about.views import about_view

urlpatterns = [
     path('', include('games.urls')),
     path('', include('users.urls')),
     path('about/', include('about.urls')),
     path('login/', LoginView.as_view(), name='login'),
	path('logout/', LogoutView.as_view(), name='logout'),
	path('signup/', SignupView.as_view(), name='signup'),
     path('accounts/', include('allauth.urls')),
     path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

handler400 = 'users.views.error_400_view'
handler404 = 'users.views.error_404_view'
handler500 = 'users.views.error_500_view'
 