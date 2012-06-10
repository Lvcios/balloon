from django.db import models

# Create your models here.
class tuit(models.Model):
	id_tweet = models.CharField(max_length = 50)
	usuario = models.CharField(max_length = 20)
	frase = models.CharField(max_length = 280)
	fechahora = models.DateTimeField('date published')

