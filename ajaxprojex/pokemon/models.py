from django.db import models
from django.contrib.auth.models import User, AbstractUser
# Create your models here.

class Player(AbstractUser):
    phone = models.CharField(max_length=12, help_text="Format should be: 650-111-2222")

class Team(models.Model):
    name = models.CharField(max_length=30)
    player = models.ForeignKey(Player, related_name='player')

    def __unicode__(self):
        return u"{}".format(self.name)

class Pokemon(models.Model):
    name = models.CharField(max_length=30)
    image = models.URLField()
    pokedex_id = models.PositiveIntegerField()  # this is the ID from the pokeapi
    team = models.ForeignKey(Team, related_name='team')

    def __unicode__(self):
        return u"{}".format(self.name)
