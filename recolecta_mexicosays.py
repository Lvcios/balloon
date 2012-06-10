#!/usr/bin/env python
# _*_ coding:utf8 _*_
from django.core.management import setup_environ
import balloon.settings
setup_environ(balloon.settings)
import time
from mexicosays.models import tuit
import tweepy


def search(request):
	t = tuit
	print 'Conexión (re)establecida'
	while True:		
		try:
			print 'Buscando'
			search = tweepy.api.search("JVM OR EPN OR AMLO OR QUADRI -filter:links -RT")
			if search:
				for tweets in search:
					try: #captura tweets
						t = tuit(id_tweet=tweets.id,usuario=tweets.from_user,frase=tweets.text,fechahora = tweets.created_at)
						if not tuit.objects.filter(id_tweet=tweets.id) and (len(t.frase)>=100):
							t.save()
							print 'Mensaje guardado'
					except:
						print 'Error al guardar el tweet. Verifique que el servidor de base de datos esté activado'				
		except:
			print 'Se ha perdido la conexión.'
			for i in range(3):
				print '...'
				time.sleep(3)
			print 'Recuperando la conexión a internet.'
						
			
search('')
