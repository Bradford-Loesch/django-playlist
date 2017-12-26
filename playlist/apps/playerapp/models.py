# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime
import bcrypt
import re

class ObjectManager(models.Manager):
    def valid_login(self, data):
        errors = []
        user_lookup = Users.objects.get(email = data['email'])
        if len(user_lookup) == 0:
            errors.append("Not a valid username and password.")
            return False, errors
        password = data['password'].encode()
        hashed = user_lookup.password.encode()
        if bcrypt.hashpw(password, hashed) == hashed:
             return True, user_lookup.id
        else:
            errors.append("Not a valid username and password.")
            return False, errors

    def valid_register(self, data):
        print "IN VALIDATION"
        email_re = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        bday = datetime.datetime.strptime(data['bday'], "%Y-%m-%d").date()
        ageday =  datetime.date.today() - datetime.timedelta(days=13*365)
        errors = []
        if len(data['first_name']) < 2:
            errors.append("First name must be at least two characters")
        if not data['first_name'].isalpha():
            errors.append("First name must be letters")
        if len(data['last_name']) < 2:
            errors.append("Last name must be at least two characters")
        if not data['last_name'].isalpha():
            errors.append("Last name must be letters")
        if not email_re.match(data['email']):
            errors.append("Must be a valid email")
        if not data['passworda'] == data['passwordb']:
            errors.append("Passwords must match")
        if len(data['passworda']) < 8:
            errors.append("Password must be at least 8 characters")
        if bday > ageday:
            errors.append("You must be 13 years old")
        if len(errors) > 0:
            return False, errors
        else:
            password = data['passworda'].encode()
            hashed = bcrypt.hashpw(password, bcrypt.gensalt())
            new_user = User.objects.create(first_name = data['first_name'], last_name = data['last_name'], email = data['email'], password = hashed, birthday = bday)
            return True, new_user
    def valid_song(self, data):
        pass
    def valid_artist(self, data):
        pass
    def encrypt(password):
        password = password.encode()
        hashed = bcrypt.hashpw(password, bcrypt.gensalt())
        return hashed
    def comparePass(password, hashed):
        password = password.encode()
        hashed = hashed.encode()
        if bcrypt.hashpw(password, hashed) == hashed:
            return True
        return False


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    birthday = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ObjectManager()

class Song(models.Model):
    title = models.CharField(max_length=255)
    length = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    writer = models.ForeignKey('Artist', related_name = 'writer')
    playlist = models.ManyToManyField('User', related_name = 'playlist')

    objects = ObjectManager()    

class Artist(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ObjectManager()
    