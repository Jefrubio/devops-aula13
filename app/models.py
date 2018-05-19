"""
Definition of models.
"""

from django.db import models

# Create your models here.
class Curso(models.Model):
    nome = models.CharField(max_length=200)
    periodo = models.CharField(max_length=50)
    instituicao = models.CharField(max_length=200)

class Vestibular(models.Model):
    nome = models.CharField(max_length=200)
   
class Candidato(models.Model):
    nome = models.CharField(max_length=100)
    RG = models.CharField(max_length=9)
    CPF = models.CharField(max_length=11)
   
class Local_Provas(models.Model):
    nome_escola = models.CharField(max_length=500)
    endereco = models.CharField(max_length=500)
    cidade = models.CharField(max_length=500)
    estado = models.CharField(max_length=50)
    

