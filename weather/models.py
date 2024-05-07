from django.db import models
from jsonfield import JSONField

class WeatherData(models.Model):
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    detailing_type = models.CharField(max_length=20, null=True, blank=True)
    data = JSONField(null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        unique_together = ('latitude', 'longitude', 'detailing_type')
