from django.db import models

class Card(models.Model):
    color = models.CharField(max_length=20, default="")
    rank = models.IntegerField(max_length=1, default="")

    def __str__(self):
        return "{} of {}".format(self.rank, self.color)        
        
