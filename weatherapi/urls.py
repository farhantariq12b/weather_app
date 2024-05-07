from django.urls import path, include
from .views import weather_api


urlpatterns = [
    path('weather-api/', weather_api, name='weather_api'),   
]
