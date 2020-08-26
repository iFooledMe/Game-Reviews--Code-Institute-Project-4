from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import DateField, DateTimeField, IntegerField, TimeField, Transform


from games.models import Game


class UserAvatar(models.Model):
    image = models.ImageField(
        upload_to='users/user_avatars/',
        max_length=255, null=True, blank=True)
    description = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.description


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_premium = models.BooleanField(default=False)
    chat_alias = models.CharField(max_length=30, null=True, blank=True)
    avatar = models.ForeignKey(
        UserAvatar,
        null=True, blank=True,
        on_delete=models.SET_NULL)
    image = models.ImageField(
        upload_to='users/user_images/',
        max_length=255, null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()


class UserCommentsScore(models.Model):
    user = models.ForeignKey(
        User,
        null=True, blank=True,
        on_delete=models.CASCADE)
    game = models.ForeignKey(
        Game,
        null=True, blank=True,
        on_delete=models.CASCADE)
    comment = models.TextField(
        max_length=300, null=True, blank=True)
    user_score = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(10)],
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        show_name = "(" + str(self.user.id) + ")" + str(self.user) + \
            "_(" + str(self.game.id) + ")" + str(self.game.title)
        return show_name
