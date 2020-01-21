from django.db import models
from produtos.models import Produto

# Create your models here.
class Venda(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    desconto = models.IntegerField()
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    formas_pagamento = (('BOLETO', 'Boleto'), ('CARTAO','Cartão'))
    forma_pagamento = models.CharField(max_length=50, choices=formas_pagamento)