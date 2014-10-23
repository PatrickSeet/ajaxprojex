from django.contrib import admin
from pokemon.models import Team
from pokemon.models import Pokemon

# Register your models here.
admin.site.register(Team)
admin.site.register(Pokemon)