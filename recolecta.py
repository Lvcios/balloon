#!/usr/bin/env python
# _*_ coding:utf8 _*_
from django.core.management import setup_environ
import balloon.settings
setup_environ(balloon.settings)
import time
from tweetminner.models import MetaD_Tuits,HashTag
import tweepy


def search(request):
	t = MetaD_Tuits
	h = HashTag
	ht = ''
	print 'Conexión (re)establecida'
	while True:		
		try:
			print 'Buscando'
			search = tweepy.api.search("JVM OR EPN OR AMLO OR QUADRI -filter:links -RT")
			if search:
				for tweets in search:
					try: #captura tweets
						t = MetaD_Tuits(Tuit_ID=tweets.id,Usuario=tweets.from_user,Frase=tweets.text,FechaHora = tweets.created_at)
						if not MetaD_Tuits.objects.filter(Tuit_ID=tweets.id):
							t.save()
							print 'Mensaje guardado'
							try:
								ht = tweets.text.split()
								for word in ht:
									if word[0] == '#':
										if not HashTag.objects.filter(HT=word.lower()):
											print 'HT Nuevo'
											h = HashTag(HT = word.lower(), Numero_De_Tuits = 1)
											h.save()
										else:
											print 'HT reconocido'
											update = HashTag.objects.get(HT=word.lower())
											n = update.Numero_De_Tuits + 1
											update = HashTag(id=update.id,HT = word.lower(), Numero_De_Tuits = n)
											update.save()
							except:
								print "Error al guardar HT's"
					except:
						print 'Error al guardar el tweet. Verifique que el servidor de base de datos esté activado'
					#captura HT's
					
				
		except:
			print 'Se ha perdido la conexión.'
			for i in range(3):
				print '...'
				time.sleep(3)
			print 'Recuperando la conexión a internet.'
						
			
search('')
