import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
import time

# Latitude of City
lat = 0 # Fix Me 
# Longitude of City
lon = 0 # Fix Me

appid = "" # Fix Me

# Link for API documentation on onecall API: https://openweathermap.org/api/one-call-api

url = "https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&exclude=current,minutely,hourly,alerts&appid={}&units=imperial".format(lat, lon, appid)

resp = requests.get(url)

data = "" # Fix Me

print(json.dumps(data, indent=2))