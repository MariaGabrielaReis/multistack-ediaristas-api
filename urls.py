from django.urls import path
from .views import HousekeepersCityList

# definição das rotas do projeto

urlpatterns = [
    path('city-housekeepers', HousekeepersCityList.as_view(), name='city-housekeepers-list')
]
