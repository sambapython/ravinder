from django.contrib import admin
from service.models import Player,Country, Match

# Register your models here.
admin.site.register(Player)
admin.site.register(Country)
admin.site.register(Match)
