from django.db import models

# Create your models here.

class Manutencao(models.Model):
    id_manutencao = models.AutoField(primary_key=True)
    empresa = models.TextField(max_length=255)
    tell = models.IntegerField()
