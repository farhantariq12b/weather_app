import requests
from django.shortcuts import render, redirect
from django.utils.timezone import now
from datetime import timedelta
from .forms import WeatherRequestForm
from .models import WeatherData
from django.conf import settings

API_KEY = settings.OPENWEATHER_API_KEY
BASE_URL = settings.BASE_URL
API_BASE_URL = settings.API_BASE_URL

def fetch_weather_data(lat, lon, data_type):
    api_key = settings.OPENWEATHER_API_KEY
    url = f"{API_BASE_URL}?lat={lat}&lon={lon}&exclude={data_type}&appid={api_key}"
    response = requests.get(url)
    return response.json()

def get_weather(request):
    if request.method == 'POST':
        form = WeatherRequestForm(request.POST)
        if form.is_valid():
            lat = form.cleaned_data['latitude']
            lon = form.cleaned_data['longitude']
            detailing = form.cleaned_data['detailing_type']

            # Check database first
            try:
                weather_data = WeatherData.objects.get(latitude=lat, longitude=lon, detailing_type=detailing)
                if now() - weather_data.last_updated > timedelta(minutes=settings.DATA_EXPIRY_TIME):
                    raise WeatherData.DoesNotExist
            except WeatherData.DoesNotExist:
                response = requests.get(BASE_URL, params={
                    'lat': lat,
                    'lon': lon,
                    'appid': API_KEY,
                    'exclude': 'minutely,hourly,daily,current' if detailing != 'all' else '',
                    'units': 'metric'
                })
                data = response.json()

                # Update or create new record
                WeatherData.objects.update_or_create(
                    latitude=lat, longitude=lon, detailing_type=detailing,
                    defaults={'data': data, 'last_updated': now()}
                )
                weather_data = WeatherData.objects.get(latitude=lat, longitude=lon, detailing_type=detailing)

            return render(request, 'weather_data.html', {'weather': weather_data})
    else:
        form = WeatherRequestForm()

    return render(request, 'weather_form.html', {'form': form})
