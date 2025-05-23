import requests
import os

def get_weather_by_location(location):
    API_KEY = "9a4dc41846bf44352b37b199a1978209"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric"
    r = requests.get(url)
    if r.status_code == 200:
        data = r.json()
        return {
            'temp': data['main']['temp'],
            'condition': data['weather'][0]['description']
        }
    return None

def validate_location(location):
    return get_weather_by_location(location) is not None
