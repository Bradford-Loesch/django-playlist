# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import bcrypt
import re

class ObjectManager(models.Manager):
    def valid_login(self, data):
        pass
    def valid_register(self, data):
        pass
    def valid_song(self, data):
        pass
    def valid_artist(self, data):
        pass


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    birtday = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ObjectManager()

class Song(models.Model):
    title = models.CharField(max_length=255)
    length = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    playlist = models.ManyToManyField('User', related_name = 'playlist')

    objects = ObjectManager()    

class Artist(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    writer = models.ForeignKey('Song', related_name = 'writer')

    objects = ObjectManager()
    