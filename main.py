import requests
import APIrequest

def obter_imagems_satelites(API_KEY, latitude, longitude):
    base_url = https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}