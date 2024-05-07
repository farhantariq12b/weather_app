
# Weather Forecast

## Description:

Weather Forecast is a Django project designed to get `current` and `3-hourly/5 days` weather data based on user' location. User has to input longitude & latitude and select the type of forecast he/she wants 

## Setup:

To set up the project, follow these steps:

### Using Virtual Environment (venv):

Create a virtual environment:
```
python -m venv weather-env
```
Activate the virtual environment:
```
source weather-env/bin/activate
```
Install dependencies from requirements.txt:
```
pip install -r requirements.txt
```

## Running the Server:

To run the server, execute the following command:
```
python manage.py runserver
```

## Usage:
Use this weather app to access current weather and forecasts powered by OpenWeatherAPI. Simply run the server, 
navigate to http://127.0.0.1:8000 in your browser, input longitude, latitude, and forecast type, and get instant weather updates.

## Dependencies:
```
asgiref==3.8.1
certifi==2024.2.2
charset-normalizer==3.3.2
Django==2.2
django-cors-headers==4.3.1
django-environ==0.11.2
djangorestframework==3.12.2
exceptiongroup==1.2.1
idna==3.7
iniconfig==2.0.0
jsonfield==3.1.0
packaging==24.0
pluggy==1.5.0
pytest==8.1.1
pytest-django==4.8.0
pytz==2024.1
requests==2.31.0
sqlparse==0.5.0
tomli==2.0.1
typing_extensions==4.11.0
urllib3==2.2.1

```

Note: Make sure to have the project dependencies installed and the server running before making requests to the APIs.
