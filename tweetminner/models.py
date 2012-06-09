from django.db import models

# Create your models here.
class MetaD_Tuits(models.Model):
	Tuit_ID = models.CharField(max_length = 50)
	Usuario = models.CharField(max_length = 20)
	Frase = models.CharField(max_length = 280)
	FechaHora = models.DateTimeField('date published')


class HashTag(models.Model):
	HT = models.CharField(max_length = 280)
	#Numero_De_Tuits = models.IntegerField()
