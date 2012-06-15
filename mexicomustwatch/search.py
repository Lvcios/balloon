# _*_ coding:utf-8 _*_
#@Lvcios
#http://lvcios.blogspot.com
import gdata.youtube
import gdata.youtube.service

def PrintVideoFeed(feed):
	for entry in feed.entry:
		PrintEntryDetails(entry)
	
def PrintEntryDetails(entry):
	#print 'Video ID: ' + entry.media.id.text
	print 'Video title: %s' % entry.media.title.text
	print 'Video published on: %s ' % entry.published.text
	print 'Video description: %s' % entry.media.description.text
	#print 'Video category: %s' % entry.media.category.text
	print 'Video tags: %s' % entry.media.keywords.text
	print 'Video watch page: %s' % entry.media.player.url
	print 'Video flash player URL: %s' % entry.GetSwfUrl()
	print 'Video duration: %s' % entry.media.duration.seconds
  # non entry.media attributes
	print 'Video view count: %s' % entry.statistics.view_count
	print 'Video rating: %s' % entry.rating.average
	print '-------------------------------------------------------------'
	
#def SearchAndPrintVideosByKeywords(list_of_search_terms):
def SearchAndPrint(list_of_search_terms):
	yt_service = gdata.youtube.service.YouTubeService()
	query = gdata.youtube.service.YouTubeVideoQuery()
	query.orderby = 'viewCount'
	query.racy = 'include'
	for search_term in list_of_search_terms:
		new_term = search_term.lower()
		query.categories.append('/%s' % new_term)
	feed = yt_service.YouTubeQuery(query)
	PrintVideoFeed(feed)	
	#SearchKeyWords(feed)
	

def SearchKeyWords(feed): #Esta funcion busca coincidencias entre las palabras que buscamos
	for entry in feed.entry:#y la descripcion del video
		description = str(entry.media.description.text)
		print description
		description = description.split()
		coincidencias = 0
		keywords = 'AMLO EPN JVM QUADRI PRI PAN PRD 132' #palabras a buscar dentro de la descripción, se puede aplicar también para 
		keywords = keywords.split() #los titulos de los videos y demás
		for i in range(len(keywords)):
			for j in range(len(description)):
				if keywords[i] == description[j]:
					print 'Coincidencia encontrada: ' + str(keywords[i])
					coincidencias = coincidencias + 1
		print 'Se encontraron ' + str(coincidencias) + ' coincidencias'
		print '-'*140

parameters = "AMLO EPN JVM QUADRI PRI PAN PRD 132"
SearchAndPrint(parameters.split())

