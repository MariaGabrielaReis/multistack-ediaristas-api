from . import cep_service
from ..models import Housekeeper
from rest_framework import serializers
import json


def to_list_housekeepers_city(cep):
    # pega o código do IBGE daquele CEP
    codigo_ibge = get_city_cep(cep)['ibge']
    # busca todas as diaristas cadastradas com aquele código
    housekeepers = Housekeeper.objects.filter(codigo_ibge=codigo_ibge).order_by('id')
    return housekeepers


def get_city_cep(cep):
    # recebe o CEP e verifica se é inválido ou se não existe
    response = cep_service.get_city_cep(cep)
    if response.status_code == 400:
        raise serializers.ValidationError('CEP inválido')
    city_api = json.loads(response.content)
    if 'erro' in city_api:
        raise serializers.ValidationError('CEP não encontrado')
    return city_api
