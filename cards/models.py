from django.db import models

class Card(models.Model):
    num = models.IntegerField()
    color = models.CharField(max_length=20, default="", blank=True)
    rank = models.CharField(max_length=1, default="", blank=True)

    def __str__(self):
        return "Card nr. {}: {}, {}".format(self.num, self.rank, self.color)        
        
