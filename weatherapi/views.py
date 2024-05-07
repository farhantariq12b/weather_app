from django.http import JsonResponse, HttpResponseBadRequest
import requests
from .models import WeatherData1
from django.utils.timezone import now
from datetime import timedelta
from django.conf import settings

API_KEY = settings.OPENWEATHER_API_KEY
BASE_URL = settings.BASE_URL

def weather_api(request):
    try:
        lat = float(request.GET.get('lat'))
        lon = float(request.GET.get('lon'))
        detailing = request.GET.get('detailing')
    except (TypeError, ValueError):
        return HttpResponseBadRequest("Invalid or missing latitude, longitude, or detailing type")

    if not detailing in ['current', 'minute', 'hourly', 'daily']:
        return HttpResponseBadRequest("Invalid detailing type")

    # Check database first
    try:
        weather_data = WeatherData1.objects.get(latitude=lat, longitude=lon, detailing_type=detailing)
        if now() - weather_data.last_updated > timedelta(minutes=settings.WEATHER_DATA_EXPIRY):
            raise WeatherData1.DoesNotExist
    except WeatherData1.DoesNotExist:
        response = requests.get(BASE_URL, params={
            'lat': lat,
            'lon': lon,
            'appid': API_KEY,
            'exclude': 'minutely,hourly,daily,current' if detailing != 'all' else '',
            'units': 'metric'
        })
        data = response.json()

        # Update or create new record
        WeatherData1.objects.update_or_create(
            latitude=lat, longitude=lon, detailing_type=detailing,
            defaults={'data': data, 'last_updated': now()}
        )
        weather_data = WeatherData1.objects.get(latitude=lat, longitude=lon, detailing_type=detailing)

    return JsonResponse(weather_data.data)
