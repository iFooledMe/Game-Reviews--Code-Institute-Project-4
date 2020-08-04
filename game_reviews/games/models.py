from django.db import models
import datetime

# Create your models here.


class Developer(models.Model):
	company_name	= models.CharField(max_length=40)
	
	def __str__(self):
		return self.company_name


class Publisher(models.Model):
	company_name	= models.CharField(max_length=40)
	
	def __str__(self):
		return self.company_name


class Pegi(models.Model):
	pegi_class = models.CharField(max_length=10)

	def __str__(self):
		return self.pegi_class


class TagCategory(models.Model):
	category_name	= models.CharField(max_length=30)

	def __str__(self):
		return self.category_name


class Tag(models.Model):
	tag_name		= models.CharField(max_length=40)
	tag_category	= models.ForeignKey(TagCategory, null=True, on_delete=models.SET_NULL)

	def __str__(self):
		return self.tag_name


class Store(models.Model):
	store_name		= models.CharField(max_length=40)

	def __str__(self):
		return self.store_name


class Platform(models.Model):
	long_name		= models.CharField(max_length=40)
	short_name		= models.CharField(max_length=10)

	def __str__(self):
		return self.long_name


class Game(models.Model):
	title 			= models.CharField(max_length=40)
	#release_date	= models.DateField(initial=date.today)
	description 	= models.TextField(max_length=500)
	description_src	= models.URLField(default='http//www.google.com')
	developer		= models.ForeignKey(Developer, null=True, on_delete=models.SET_NULL) 
	publisher		= models.ForeignKey(Publisher, null=True, on_delete=models.SET_NULL) 
	pegi 			= models.ForeignKey(Pegi, null=True, on_delete=models.SET_NULL)
	platforms		= models.ManyToManyField(Platform) 
	tags 			= models.ManyToManyField(Tag)
	stores			= models.ManyToManyField(Store)

