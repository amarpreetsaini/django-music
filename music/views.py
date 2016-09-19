from django.shortcuts import render
from .models import Singer,Songs,Albums

# Create your views here.

def index(request):
	all_singers = Singer.objects.all()
	return render(request,'music/index.html',{'singers':all_singers})
	
def details(request,singer_id):
	singer_Albums = Albums.objects.filter(songs__singers__id=singer_id)
	return render(request,'music/details.html',{'singer_Albums':singer_Albums})

def songs(request,singer_id):
	all_Songs = Songs.objects.filter(singers__id=singer_id)
	return render(request,'music/songs/songs.html',{'all_Songs':all_Songs})
	
def albums(request,album_id):
	all_Albums = Albums.objects.filter(id=album_id)
	return render(request,'music/albums/album_song.html',{'all_Albums':all_Albums})
