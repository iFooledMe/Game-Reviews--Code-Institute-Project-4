from django.shortcuts import render
from .models import Info

def about_view(request, *args, **kwargs):
    info = Info.objects.all()

    context = {
        'info': info,
    }

    return render(request, "about.html", context)
