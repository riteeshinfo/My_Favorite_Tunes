# TuneTracker/forms.py

from django.forms import ModelForm
from .models import Artist, Song

class SongForm(ModelForm):
    class Meta:
        model = Song
        fields = ['title', 'artist']

class ArtistForm(ModelForm):
    class Meta:
        model = Artist
        fields = ['name']
 