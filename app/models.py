from cgitb import text
from nturl2path import url2pathname
from statistics import mode
from turtle import title
from unicodedata import name
from django.db import models


class Song(models.Model):
    name = models.CharField('曲名', max_length=64)
    composer = models.CharField('作曲者', max_length=32)
    lyrist = models.CharField('作詞者', max_length=32)
    lyrics = models.TextField('歌詞')

    def __self__(self):
        return self.name


class Youtube(models.Model):
    url = models.URLField('URL')
    song = models.ForeignKey(Song, on_delete=models.PROTECT)
