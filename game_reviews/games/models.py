from django.db import models
import datetime

# region ==== S U B  M O D E L S ============================================


class Developer(models.Model):
    name = models.CharField(max_length=40)
    short_name = models.CharField(max_length=20, null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    logo_icon = models.CharField(max_length=50, null=True, blank=True)
    show_icon = models.BooleanField(default=False)
    logo_img = models.ImageField(
        upload_to='developers/logotypes/', null=True, blank=True)
    show_img = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=40)
    short_name = models.CharField(max_length=20, null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    logo_icon = models.CharField(max_length=50, null=True, blank=True)
    show_icon = models.BooleanField(default=False)
    logo_img = models.ImageField(
        upload_to='publishers/logotypes/', null=True, blank=True)
    show_img = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Pegi(models.Model):
    pegi_class = models.CharField(max_length=10)
    thumb_img = models.ImageField(upload_to='pegi')

    def __str__(self):
        return self.pegi_class


class GenreTag(models.Model):
    long_name = models.CharField(max_length=40)
    short_name = models.CharField(max_length=10, null=True, blank=True)
    show_name = models.BooleanField(default=True)
    tag_icon = models.CharField(max_length=40, null=True, blank=True)
    show_icon = models.BooleanField(default=False)
    tag_category = models.CharField(max_length=40, default="genre")

    def __str__(self):
        return self.long_name


class ThemeTag(models.Model):
    long_name = models.CharField(max_length=40)
    short_name = models.CharField(max_length=10, null=True, blank=True)
    show_name = models.BooleanField(default=True)
    tag_icon = models.CharField(max_length=40, null=True, blank=True)
    show_icon = models.BooleanField(default=False)
    tag_category = models.CharField(max_length=40, default="theme")

    def __str__(self):
        return self.long_name


class MiscTag(models.Model):
    long_name = models.CharField(max_length=40)
    short_name = models.CharField(max_length=10, null=True, blank=True)
    show_name = models.BooleanField(default=True)
    tag_icon = models.CharField(max_length=40, null=True, blank=True)
    show_icon = models.BooleanField(default=False)
    tag_category = models.CharField(max_length=40, default="misc")

    def __str__(self):
        return self.long_name


class Store(models.Model):
    name = models.CharField(max_length=40)
    short_name = models.CharField(max_length=20, null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    logo_icon = models.CharField(max_length=50, null=True, blank=True)
    show_icon = models.BooleanField(default=False)
    logo_img = models.ImageField(
        upload_to='stores/logotypes/', null=True, blank=True)
    show_img = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Platform(models.Model):
    long_name = models.CharField(max_length=40)
    short_name = models.CharField(max_length=10)
    logo_icon = models.CharField(max_length=50, null=True, blank=True)
    show_icon = models.BooleanField(default=True)
    logo_img = models.ImageField(
        upload_to='platforms/logotypes/', null=True, blank=True)
    show_img = models.BooleanField(default=False)

    def __str__(self):
        return self.long_name
# endregion
# ============================================================================


class Game(models.Model):
    title = models.CharField(max_length=40)
    thumb_img = models.ImageField(
        upload_to='game_thumbs/', null=True, blank=True)
    show_img = models.BooleanField(default=True)
    release_date = models.DateField(null=True, blank=True)
    description = models.TextField(max_length=5000, null=True, blank=True)
    description_src_name = models.CharField(
        max_length=40, null=True, blank=True)
    description_src_url = models.URLField(null=True, blank=True)
    developer = models.ForeignKey(
        Developer, null=True, blank=True, on_delete=models.SET_NULL)
    publisher = models.ForeignKey(
        Publisher, null=True, blank=True, on_delete=models.SET_NULL)
    pegi = models.ForeignKey(
        Pegi, null=True, blank=True, on_delete=models.SET_NULL)
    platforms = models.ManyToManyField(Platform, blank=True)
    genre_tags = models.ManyToManyField(GenreTag, blank=True)
    theme_tags = models.ManyToManyField(ThemeTag, blank=True)
    misc_tags = models.ManyToManyField(MiscTag, blank=True)
    stores = models.ManyToManyField(Store, blank=True)

    def __str__(self):
        return self.title
