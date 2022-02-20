from cgitb import text
from nturl2path import url2pathname
from statistics import mode
from turtle import title
from unicodedata import name
from django.db import models


class Person(models.Model):
    name = models.CharField('名前', max_length=32)

    def __str__(self):
        return self.name


class Artist(models.Model):
    name = models.CharField('アーティスト名', max_length=32)

    def __str__(self):
        return self.name


class Song(models.Model):
    name = models.CharField('曲名', max_length=64)
    composer = models.ForeignKey(
        Person, verbose_name='作曲者', max_length=32, on_delete=models.PROTECT, related_name='composer'
    )
    lyrist = models.ForeignKey(
        Person, verbose_name='作詞者', max_length=32, on_delete=models.PROTECT, related_name='lyrist'
    )
    artist = models.ForeignKey(
        Artist, verbose_name='アーティスト', max_length=32, on_delete=models.PROTECT, related_name='artist'
    )
#    lyrics = models.TextField('歌詞')

    def __str__(self):
        return '{0} {1} {2} {3}'.format(self.name, self.composer, self.lyrist, self.artist)


class Youtube(models.Model):
    url = models.URLField('URL')
    song = models.ForeignKey(Song, on_delete=models.PROTECT)

    def __str__(self):
        return self.url
