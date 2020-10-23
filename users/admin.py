from django.contrib import admin
from .models import UserProfile, UserCommentsScore, UserAvatar

admin.site.register(UserProfile)
admin.site.register(UserCommentsScore)
admin.site.register(UserAvatar)
