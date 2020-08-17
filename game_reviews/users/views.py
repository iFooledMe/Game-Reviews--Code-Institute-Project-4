from django.shortcuts import render

from .models import UserProfile


def user_profile_view(request, *args, **kwargs):
    context = {

    }
    return render(request, "user_profile.html", context)
