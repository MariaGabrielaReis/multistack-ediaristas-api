from rest_framework import serializers
from painel_administrativo.models import Housekeeper


class HousekeeperCitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Housekeeper
        fields = ('nome_completo', 'foto', 'cidade')
