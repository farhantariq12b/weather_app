from rest_framework import serializers
from .models import WeatherData1

class WeatherData1Serializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherData1
        fields = '__all__'
