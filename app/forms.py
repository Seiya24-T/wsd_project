from dataclasses import fields
from pyexpat import model
from statistics import mode
from django import forms
from .models import Song, Youtube


class SongCreateForm(forms.ModelForm):

    class Meta:
        model = Song
        fields = '__all__'


class AddYoutubeForm(forms.ModelForm):

    class Meta:
        model = Youtube
        fields = ('url',)
