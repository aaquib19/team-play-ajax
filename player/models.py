from django.db import models

# Create your models here.
class Player(models.Model):
    pname = models.CharField(max_length=50)
    hscore = models.IntegerField()
    age = models.IntegerField()

    def __str__(self):
       return self.pname