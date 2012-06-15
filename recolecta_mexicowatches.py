#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from django.core.management import setup_environ
import balloon.settings
setup_environ(balloon.settings)
import time
from mexicomustwatch.models import video
import gdata.youtube
import gdata.youtube.service

def search(list_of_search_terms):
#def SearchAndPrint(list_of_search_terms):
	yt_service = gdata.youtube.service.YouTubeService()
	query = gdata.youtube.service.YouTubeVideoQuery()
	query.orderby = 'viewCount'
	query.racy = 'include'
	for search_term in list_of_search_terms:
		new_term = search_term.lower()
		query.categories.append('/%s' % new_term)
	feed = yt_service.YouTubeQuery(query)
	for entry in feed.entry:
		#print 'Video title: %s' % entry.media.title.text
		#print 'Video description: %s' % entry.media.description.text
		#print 'Video watch page: %s' % entry.media.player.url
		#print 'Video flash player URL: %s' % entry.GetSwfUrl()
		#print 'Video view count: %s' % entry.statistics.view_count
		#print 'Video rating: %s' % entry.rating.average
		try:
			v = video(id_video = entry.media.player.url, titulo = entry.media.title.text , descripcion = entry.media.description.text, url = entry.GetSwfUrl(), vistas = str(entry.statistics.view_count), rating = str(entry.rating.average))
			if not video.objects.filter(id_video = entry.media.player.url):
				v.save()
		except:
			print 'no se pudo guardar video'
	
parameters = "AMLO EPN JVM QUADRI PRI PAN PRD 132"
search(parameters.split())
