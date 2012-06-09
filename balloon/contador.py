#!/usr/bin/env python
# _*_ coding:utf8 _*_
from django.core.management import setup_environ
import settings
setup_environ(settings)
import time
from tweetminner.models import MetaD_Tuits,HashTag
import tweepy


def search(request):
	while True:
		search = tweepy.api.search("JVM OR EPN OR AMLO OR QUADRI -filter:links -RT")
		if search:
			for tweets in search:
				ht = tweets.text.lower()
				ht = tweets.text.split()
				for word in ht:
					print word
					if word[0] == '#':
						if not HashTag.objects.filter(HT=word.lower()):
							print 'Es un HT NUEVO'
							time.sleep(3)
							h = HashTag(HT = word.lower(), Numero_De_Tuits = 1)
							h.save()
							print 'HT registrado'
						else:
							print 'Es un HT YA REGISTRADO'
							update = HashTag.objects.get(HT=word.lower())
							#print update.Numero_De_Tuits
							#print update.id
							n = update.Numero_De_Tuits + 1
							#print n
							update = HashTag(id=update.id,HT = word.lower(), Numero_De_Tuits = n)
							update.save()
							time.sleep(3)
						

						
			
search('')
