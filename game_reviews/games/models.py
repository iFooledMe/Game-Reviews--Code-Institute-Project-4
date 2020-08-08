from django.db import models
import datetime

# region ==== SUB-CLASSES =================================================================


class Developer(models.Model):
    long_name = models.CharField(max_length=40)
    short_name = models.CharField(max_length=20, null=True, blank=True)
    web_url = models.URLField(max_length=200, null=True, blank=True)
    logo_img = models.ImageField(
        upload_to='developers/logo_images/',
        max_length=255, null=True, blank=True)
    show_logo_img = models.BooleanField(default=False)
    logo_icon = models.CharField(max_length=50, null=True, blank=True)
    show_logo_icon = models.BooleanField(default=False)

    def __str__(self):
        return self.long_name


class Publisher(models.Model):
    long_name = models.CharField(max_length=40)
    short_name = models.CharField(max_length=20, null=True, blank=True)
    web_url = models.URLField(max_length=200, null=True, blank=True)
    logo_img = models.ImageField(
        upload_to='publishers/logo_images/',
        max_length=255, null=True, blank=True)
    show_logo_img = models.BooleanField(default=False)
    logo_icon = models.CharField(max_length=50, null=True, blank=True)
    show_logo_icon = models.BooleanField(default=False)

    def __str__(self):
        return self.long_name


class Pegi(models.Model):
    pegi_class = models.CharField(max_length=10)
    short_name = models.CharField(max_length=10, null=True, blank=True)
    pegi_img = models.ImageField(
        upload_to='pegi/pegi_images/',
        max_length=255, null=True, blank=True)

    def __str__(self):
        return self.pegi_class


class GenreTag(models.Model):
    long_name = models.CharField(max_length=40)
    short_name = models.CharField(max_length=40, null=True, blank=True)
    show_name = models.BooleanField(default=True)
    icon = models.CharField(max_length=50, null=True, blank=True)
    show_icon = models.BooleanField(default=False)
    tag_category = models.CharField(max_length=40, default='genre')

    def __str__(self):
        return self.long_name


class ThemeTag(models.Model):
    long_name = models.CharField(max_length=40)
    short_name = models.CharField(max_length=40, null=True, blank=True)
    show_name = models.BooleanField(default=True)
    icon = models.CharField(max_length=50, null=True, blank=True)
    show_icon = models.BooleanField(default=False)
    tag_category = models.CharField(max_length=40, default='theme')

    def __str__(self):
        return self.long_name


class MiscTag(models.Model):
    long_name = models.CharField(max_length=40)
    short_name = models.CharField(max_length=40, null=True, blank=True)
    show_name = models.BooleanField(default=True)
    icon = models.CharField(max_length=50, null=True, blank=True)
    show_icon = models.BooleanField(default=False)
    tag_category = models.CharField(max_length=40, default='misc')

    def __str__(self):
        return self.long_name


class Store(models.Model):
    long_name = models.CharField(max_length=40)
    short_name = models.CharField(max_length=20, null=True, blank=True)
    web_url = models.URLField(max_length=200, null=True, blank=True)
    logo_img = models.ImageField(
        upload_to='stores/logo_images/',
        max_length=255, null=True, blank=True)
    show_logo_img = models.BooleanField(default=False)
    logo_icon = models.CharField(max_length=50, null=True, blank=True)
    show_logo_icon = models.BooleanField(default=False)

    def __str__(self):
        return self.long_name


class Platform(models.Model):
    long_name = models.CharField(max_length=40)
    short_name = models.CharField(max_length=10)
    icon = models.CharField(max_length=50, null=True, blank=True)
    show_icon = models.BooleanField(default=True)
    img = models.ImageField(
        upload_to='platforms/platform_images/', max_length=255, null=True, blank=True)
    show_img = models.BooleanField(default=False)

    def __str__(self):
        return self.long_name

# endregion
# ==========================================================================================


class Game(models.Model):
    title = models.CharField(
        max_length=40)
    thumb_img = models.ImageField(
        upload_to='games/thumb_images/',
        max_length=255, null=True, blank=True)
    release_date = models.DateField(
        null=True, blank=True)
    description = models.TextField(
        max_length=5000, null=True, blank=True)
    description_src = models.CharField(
        max_length=40, null=True, blank=True)
    description_src_url = models.URLField(
        max_length=255, null=True, blank=True)
    developer = models.ForeignKey(
        Developer,
        null=True, blank=True,
        on_delete=models.SET_NULL)
    publisher = models.ForeignKey(
        Publisher,
        null=True, blank=True,
        on_delete=models.SET_NULL)
    pegi = models.ForeignKey(
        Pegi,
        null=True, blank=True,
        on_delete=models.SET_NULL)
    platforms = models.ManyToManyField(Platform)
    genre_tags = models.ManyToManyField(GenreTag)
    theme_tags = models.ManyToManyField(ThemeTag)
    misc_tags = models.ManyToManyField(MiscTag)
    stores = models.ManyToManyField(Store)

    def __str__(self):
        return self.title
