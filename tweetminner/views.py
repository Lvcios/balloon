# Create your views here.
from django.db.models import Q
from django.shortcuts import render_to_response
from models import MetaD_Tuits

def tweets(request):
	lista_tweets = MetaD_Tuits.objects.all()
	#lista_tweets = MetaD_Tuits.objects.extra(where Fr)
	return render_to_response('tweets.html',{'lista_tweets':lista_tweets})
