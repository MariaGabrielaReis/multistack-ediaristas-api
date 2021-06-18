from rest_framework import serializers
from painel_administrativo.models import Housekeeper
import random


class HousekeeperCitySerializer(serializers.ModelSerializer):
    reputacao = serializers.SerializerMethodField()

    class Meta:
        model = Housekeeper
        fields = ('nome_completo', 'foto', 'cidade', 'reputacao')

    def get_reputacao(self, obj):
        return random.randint(0, 5)

