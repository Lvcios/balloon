#!/usr/bin/env python
# _*_ coding:utf8 _*_
from django.core.management import setup_environ
import settings
setup_environ(settings)
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
					except:
						print 'Error al guardar el tweet. Verifique que el servidor de base de datos esté activado'
					#captura HT's
					try:
						ht = tweets.text.lower()
						ht = tweets.text.split()
						for word in ht:
							if word[0] == '#': #verificamos que se trate de un ht
								#verificar si ya está en la bd
								if not HashTag.objects.filter(HT=word):
									h = HashTag(HT = word)
									h.save()
					except:
						print "Error al guardar HT's"
				
		except:
			print 'Se ha perdido la conexión.'
			for i in range(3):
				print '...'
				time.sleep(3)
			print 'Recuperando la conexión a internet.'
						
			
search('')
