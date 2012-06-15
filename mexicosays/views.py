# Create your views here.
from django.db.models import Q
from django.shortcuts import render_to_response
from models import tuit

def tweets(request):
	lista_tweets = tuit.objects.all()
	#lista_tweets = MetaD_Tuits.objects.extra(where Fr)
	return render_to_response('tweets.html',{'lista_tweets':lista_tweets})

def mexicosays(request):
	parametros = "AMLO OR JVM OR QUARI OR EPN -RT -filter:links"
	return render_to_response('mexicosays.html',{'parametros':parametros})


def carrusel(request):
	lista_tweets = tuit.objects.all()
	#lista_tweets = MetaD_Tuits.objects.extra(where Fr)
	return render_to_response('index.html',{'lista_tweets':lista_tweets})
