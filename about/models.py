from django.db import models

class Info(models.Model):
	intro_header = models.CharField(max_length=100, null=True, blank=True)
	intro_text = models.TextField(
        max_length=10000, null=True, blank=True)
	intro_slogan = models.CharField(max_length=200, null=True, blank=True)
	intro_img = models.ImageField(
        upload_to='about/',
        max_length=255, null=True, blank=True)
	intro_img_alt = models.CharField(max_length=100, null=True, blank=True)

	reviews_info_header = models.CharField(max_length=100, null=True, blank=True)
	reviews_info_text = models.TextField(
        max_length=10000, null=True, blank=True)
	reviews_info_img = models.ImageField(
        upload_to='about/',
        max_length=255, null=True, blank=True)
	reviews_info_img_alt = models.CharField(max_length=100, null=True, blank=True)

	score_info_header = models.CharField(max_length=100, null=True, blank=True)
	score_info_text = models.TextField(
        max_length=10000, null=True, blank=True)
	score_info_img = models.ImageField(
        upload_to='about/',
        max_length=255, null=True, blank=True)
	score_info_img_alt = models.CharField(max_length=100, null=True, blank=True)

	game_info_header = models.CharField(max_length=100, null=True, blank=True)
	game_info_text = models.TextField(
        max_length=10000, null=True, blank=True)
	game_info_img = models.ImageField(
        upload_to='about/',
        max_length=255, null=True, blank=True)
	game_info_img_alt = models.CharField(max_length=100, null=True, blank=True)

	users_info_header = models.CharField(max_length=100, null=True, blank=True)
	users_info_text = models.TextField(
        max_length=10000, null=True, blank=True)
	users_info_img = models.ImageField(
        upload_to='about/',
        max_length=255, null=True, blank=True)
	users_info_img_alt = models.CharField(max_length=100, null=True, blank=True)

class About(models.Model):
	intro_header = models.CharField(max_length=100, null=True, blank=True)
	intro_text = models.TextField(
        max_length=10000, null=True, blank=True)
	intro_img = models.ImageField(
        upload_to='about/',
        max_length=255, null=True, blank=True)
	intro_img_alt = models.CharField(max_length=100, null=True, blank=True)

	reviews_info_header = models.CharField(max_length=100, null=True, blank=True)
	reviews_info_text = models.TextField(
        max_length=10000, null=True, blank=True)
	reviews_info_img = models.ImageField(
        upload_to='about/',
        max_length=255, null=True, blank=True)
	reviews_info_img_alt = models.CharField(max_length=100, null=True, blank=True)

	score_info_header = models.CharField(max_length=100, null=True, blank=True)
	score_info_text = models.TextField(
        max_length=10000, null=True, blank=True)
	score_info_img = models.ImageField(
        upload_to='about/',
        max_length=255, null=True, blank=True)
	score_info_img_alt = models.CharField(max_length=100, null=True, blank=True)

	game_info_header = models.CharField(max_length=100, null=True, blank=True)
	game_info_text = models.TextField(
        max_length=10000, null=True, blank=True)
	game_info_img = models.ImageField(
        upload_to='about/',
        max_length=255, null=True, blank=True)
	game_info_img_alt = models.CharField(max_length=100, null=True, blank=True)

	users_info_header = models.CharField(max_length=100, null=True, blank=True)
	users_info_text = models.TextField(
        max_length=10000, null=True, blank=True)
	users_info_img = models.ImageField(
        upload_to='about/',
        max_length=255, null=True, blank=True)
	users_info_img_alt = models.CharField(max_length=100, null=True, blank=True)