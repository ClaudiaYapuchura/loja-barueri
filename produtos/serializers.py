from rest_framework import serializers
from produtos.models import Produto

class ProdutoSerializer(serializers.Serializer):
    nome = serializers.CharField(max_length=255)
    valor = serializers.DecimalField(max_digits=10, decimal_places=2)
    marca = serializers.CharField(max_length=255)
    tipo = serializers.ChoiceField(choices=Produto.tipos)
    descricao = serializers.CharField()
    quantidade = serializers.IntegerField()

    def create(self, validated_data):
        produto = Produto.objects.create(**validated_data)
        return produto

    def update(self, instance, validated_data):
        instance.nome = validated_data.get('nome', instance.nome)
        instance.valor = validated_data.get('valor', instance.valor)
        instance.marca = validated_data.get('marca', instance.marca)
        instance.tipo = validated_data.get('tipo', instance.tipo)
        instance.descricao = validated_data.get('descricao', instance.descricao)
        instance.quantidade = validated_data.get('quantidade', instance.quantidade)
        instance.save()
        return instance

