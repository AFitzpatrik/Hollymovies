from django.contrib import admin

from viewer.models import Genre, Country, Creator

admin.site.register(Genre)
admin.site.register(Country)
admin.site.register(Creator)