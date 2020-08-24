from django.contrib import admin
from .models import UserProfile, UserCommentsScore

admin.site.register(UserProfile)
admin.site.register(UserCommentsScore)
