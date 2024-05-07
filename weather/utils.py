import requests
from datetime import datetime, timedelta
from django.conf import settings
from .models import WeatherData
import pytz

def fetch_weather_data(lat, lon, data_type):
    api_key = settings.OPENWEATHER_API_KEY
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&exclude={data_type}&appid={api_key}"
    response = requests.get(url)
    return response.json()

def get_or_fetch_weather(lat, lon, data_type):
    # Check if the data is in the DB and still fresh
    try:
        utc=pytz.UTC
        weather = WeatherData.objects.get(latitude=lat, longitude=lon, data_type=data_type)

        weather.last_updated = utc.localize(weather.last_updated) 
        now_time = utc.localize(datetime.now()) 

        if weather.last_updated < now_time - timedelta(minutes=settings.DATA_EXPIRY_TIME):
            raise ValueError("Data is stale, fetching new data.")
    except (WeatherData.DoesNotExist, ValueError):
        data = fetch_weather_data(lat, lon, data_type)
        weather, created = WeatherData.objects.update_or_create(
            latitude=lat, longitude=lon, data_type=data_type,
            defaults={'data': data}
        )
    return weather.data
