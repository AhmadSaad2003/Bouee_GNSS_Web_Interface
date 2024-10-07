from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Bouee(models.Model):
    name=models.CharField(max_length=25)
    dateofcreation=models.CharField(max_length=25)
    serienumber=models.CharField(max_length=20)
    country=models.CharField(max_length=20)

    def __str__(self):
        return self.name

class DonneesGnss(models.Model):
    date=models.CharField(max_length=30)
    lattitude=models.CharField(max_length=10)
    longitude=models.CharField(max_length=10)
    altitude=models.CharField(max_length=10)
    nombredesattelite=models.CharField(max_length=10)
    bouee=models.ForeignKey(Bouee, on_delete=models.CASCADE)

    def __str__(self):
        return self.date
    
class DonneesCapteures(models.Model):
    date=models.CharField(max_length=30)
    temp=models.FloatField(max_length=10)
    hum=models.FloatField(max_length=10)
    press=models.FloatField(max_length=10)
    bouee=models.ForeignKey(Bouee, on_delete=models.CASCADE)

    def __str__(self):
        return self.date