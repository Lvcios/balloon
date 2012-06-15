# Create your views here.
# _*_ coding:utf-8 _*_
from django.db.models import Q
from django.shortcuts import render_to_response
from models import video

def mexicomustwatch(request):
	lista_videos = video.objects.all()
	return render_to_response('mexicomustwatch.html',{'lista_videos':lista_videos})
	
	
