from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .services.city_attendance_service import to_list_housekeepers_city
from .serializers import city_housekeepers_serializer


class HousekeepersCityList(APIView):
    def get(self, request, format=None):
        # pega o CEP da url
        cep = self.request.query_params.get('cep', None)
        # busca todas as diaristas daquele código do IBGE do CEP
        housekeepers = to_list_housekeepers_city(cep)
        # faz o retorno dos dados das diaristas
        serializer = city_housekeepers_serializer.HousekeeperCitySerializer(housekeepers, many=True,
                                                                            context={"request": request})
        return Response(serializer.data)

