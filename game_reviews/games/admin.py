from django.contrib import admin
from .models import Game, Developer, Publisher, Pegi, Store, Platform, GenreTag, ThemeTag, MiscTag

admin.site.register(Game)
admin.site.register(Developer)
admin.site.register(Publisher)
admin.site.register(Pegi)
admin.site.register(Store)
admin.site.register(Platform)
admin.site.register(GenreTag)
admin.site.register(ThemeTag)
admin.site.register(MiscTag)
