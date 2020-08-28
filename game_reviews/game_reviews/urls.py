"""game_reviews URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include

from allauth.account.views import LoginView, SignupView, LogoutView
from games import views
from users.views import user_profile_view, pay_thankyou_view


urlpatterns = [
    path('', views.game_list_view, name='game_list'),
    path('game_details/<int:game_id>',
         views.game_details_view, name='game_details'),
    path('add_comment', views.add_comment, name='add_comment'),
    path('edit_comment', views.edit_comment, name='edit_comment'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('signup', SignupView.as_view(), name='signup'),
    path('userprofile', user_profile_view, name='userprofile'),
    path('pay_thankyou', pay_thankyou_view, name='pay_thankyou'),
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
