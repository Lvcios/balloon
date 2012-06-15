from django.db import models

# Create your models here.
class video(models.Model):
	id_video = models.URLField()
	titulo = models.CharField(max_length = 200)
	descripcion = models.TextField()
	url = models.URLField()
	vistas = models.CharField(max_length = 20)
	rating = models.CharField(max_length = 20)

