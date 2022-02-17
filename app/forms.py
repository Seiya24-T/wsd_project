from dataclasses import fields
from pyexpat import model
from statistics import mode
from django import forms
from .models import Song, Youtube, Person, Artist


class SongCreateForm(forms.ModelForm):

    class Meta:
        model = Song
        fields = '__all__'


class AddYoutubeForm(forms.ModelForm):

    class Meta:
        model = Youtube
        fields = ('url',)


class AddPersonForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = '__all__'


class AddArtistForm(forms.ModelForm):

    class Meta:
        model = Artist
        fields = '__all__'
        