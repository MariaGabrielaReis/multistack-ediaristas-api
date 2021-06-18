from django.shortcuts import render
from rest_framework.views import APIView


class HousekeepersCityList(APIView):
    def get(self, request, format=None):
        cep = self.request.query_params.get('cep', None)
