from django.db import models

# Create your models here.
class Game(models.Model):
	title 			= models.CharField(max_length=40)
	description 	= models.TextField()