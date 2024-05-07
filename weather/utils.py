# import requests
# from django.conf import settings

# def fetch_weather_data(lat, lon, detail_type):
#     api_key = settings.OPENWEATHER_API_KEY
#     base_url = "https://api.openweathermap.org/data/2.5/onecall"
#     params = {
#         'lat': lat,
#         'lon': lon,
#         'appid': api_key,
#         'exclude': 'current,minutely,hourly,daily'[:-len(detail_type)],
#     }
#     response = requests.get(base_url, params=params)
#     return response.json()



import requests
from datetime import datetime, timedelta
from django.conf import settings
from .models import WeatherData
import pytz


def fetch_weather_data(lat, lon, data_type):
    api_key = settings.OPENWEATHER_API_KEY

    # print(lat)
    # print(lon)
    # print(data_type)
    # print(api_key)
    # # url = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={data_type}&appid={api_key}"
    # #url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={data_type}&appid={api_key}"
    # #url = f"https://api.openweathermap.org/data/2.5/onecall?lat=33.44&lon=-94.04&exclude=daily&appid={api_key}"
    # #url = f"https://api.openweathermap.org/data/2.5/weather?q=${'*berlin*'}&appid=${api_key}&units=metric"
    

    # #url = f"https://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID={api_key}"
    # #url = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=minutely,hourly,daily,alerts&appid={api_key}"

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
