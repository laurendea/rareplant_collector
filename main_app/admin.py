from django.contrib import admin

# import your models here
from .models import RarePlant, PlantCultivation, PlantOrigin, PlantNurture, MusicPlaylist

# Register your models here
admin.site.register(RarePlant)
admin.site.register(PlantCultivation)
admin.site.register(PlantOrigin)
admin.site.register(PlantNurture)
admin.site.register(MusicPlaylist)
