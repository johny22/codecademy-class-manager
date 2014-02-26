# -*- coding: utf-8 -*-

from django.db import models

class Perfil(models.Model):
    nome = models.CharField(max_length=100)
    melhorP = models.IntegerField()
    hoje = models.IntegerField()
    dias_seg = models.IntegerField()
    total_ponts = models.IntegerField()

    def __unicode__(self):
        return self.nome


class Achievements(models.Model):
    perfil = models.ForeignKey(Perfil)
    nome = models.CharField(max_length=100)
    data = models.DateTimeField('Data da conquista')
    
    def __unicode__(self):
        return self.nome

class Track(models.Model):
    perfil = models.ForeignKey(Perfil)
    nome = models.CharField(max_length=100)
    percent = models.IntegerField()
    data = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.nome


class History(models.Model):
    perfil = models.ForeignKey(Perfil)
    melhorP = models.IntegerField()
    hoje = models.IntegerField()
    dias_seg = models.IntegerField()
    total_ponts = models.IntegerField()
    data_extract = models.DateTimeField('Data de extração')

    def __unicode__(self):
        return unicode(self.data_extract)
