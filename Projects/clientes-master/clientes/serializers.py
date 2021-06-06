from rest_framework import serializers
from clientes.models import Cliente
from clientes.validator import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    
    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({"cpf":"Número de CPF inválido."})
        

        if not nome_valido(data['nome']):
            raise serializers.ValidationError({"nome":"Permitido apenas letras!"})


        if not rg_valido(data['rg']):
            raise serializers.ValidationError({"rg":"Campo 'RG' deve conter 9 dígitos."})


        if not celular_valido(data['celular']):
            raise serializers.ValidationError({"celular": "Campo 'Celular' deve seguir modelo: (11) 91234-5678."})
                
        return data

