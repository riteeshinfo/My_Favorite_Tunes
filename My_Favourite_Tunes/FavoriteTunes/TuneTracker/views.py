from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Song,Artist
from .forms import SongForm,ArtistForm

def List(request):
    songs=Song.objects.all()
    return render(request,'song_list.html',{'songs':songs })
    
def song_detail(request, song_id):
    song = Song.objects.get(pk=song_id)
    return render(request, 'song_detail.html', {'songs': song})
def song_list(request):
    songs = Song.objects.all()

    if request.method == 'POST':
        existing_data=Song.objects.get()
        song_form = SongForm(request.POST,instance=existing_data)
        artist_form = ArtistForm(request.POST,instance=existing_data)

        if song_form.is_valid() and artist_form.is_valid():
            artist = artist_form.save()
            song = song_form.save()
            song.artist = artist
            song.save()
            songs = Song.objects.all()  
    else:
        song_form = SongForm()
        artist_form = ArtistForm()


    

    return render(request, 'song_list.html', {'songs': songs, 'song_form': song_form, 'artist_form': artist_form})