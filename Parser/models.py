from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    melhorP = models.IntegerField()
    hoje = models.IntegerField()
    dias_seg = models.IntegerField()
    total_ponts = models.IntegerField()
