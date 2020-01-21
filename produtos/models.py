from django.db import models

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    marca = models.CharField(max_length=255)
    tipos = (('Eletronico','ELETRONICO'), ('Automotivo', 'AUTOMOTIVO'))
    tipo = models.CharField(max_length=100, choices=tipos)
    descricao = models.TextField()
    quantidade = models.IntegerField()