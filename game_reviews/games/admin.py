from django.contrib import admin
from .models import Game, Developer, Publisher, Pegi, TagCategory, Tag, Store, Platform 

# Register your models here.
admin.site.register(Game)
admin.site.register(Developer)
admin.site.register(Publisher)
admin.site.register(Pegi)
admin.site.register(TagCategory)
admin.site.register(Tag)
admin.site.register(Store)
admin.site.register(Platform)
