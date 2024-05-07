from django import forms

class WeatherRequestForm(forms.Form):
    latitude = forms.FloatField(label='Latitude', widget=forms.NumberInput(attrs={'placeholder': 'Enter Latitude'}))
    longitude = forms.FloatField(label='Longitude', widget=forms.NumberInput(attrs={'placeholder': 'Enter Longitude'}))
    detailing_type = forms.ChoiceField(choices=[
        ('current', 'Current'),
        ('minute', 'Minute-by-minute'),
        ('hourly', 'Hourly'),
        ('daily', 'Daily')
    ], label='Detailing Type')
