from rest_framework import serializers
from ..models import Housekeeper


class HousekeeperCitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Housekeeper
        fiels = ('nome_completo', 'foto', 'cidade')