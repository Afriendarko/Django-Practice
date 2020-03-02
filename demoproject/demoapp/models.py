from django.db import models


# Create your models here.
class Musician1(models.Model):

    Artist = models.CharField(primary_key=True, max_length=50)
    instrument = models.CharField(max_length=100)
    charges = models.IntegerField()
    contact = models.IntegerField(unique=True)

    def __str__(self):
        return self.Artist

class venue(models.Model):
    Artist_name = models.ForeignKey(Musician1, on_delete=models.PROTECT)
    Name = models.CharField(unique=True, max_length=50)

    def __str__(self):
        return self.Name

