from django.db import models

# Create your models here.
from player.models import Player

class Team(models.Model):
    tname = models.CharField(max_length=100)
    player= models.ManyToManyField(Player)
    def __str__(self):
        return self.tname