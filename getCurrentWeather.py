import requests
import json

# City Name to search here
cityName = "Boston"

# Add your API key here
appid = ""

# Link for API documentation on current Weather Data API: https://openweathermap.org/current
url = ""

# Use requests module to get REST API call from url
resp = requests.get(url)

# Convert resp to json readable data format
data = resp.json()

print(json.dumps(data, indent=2))

# Pull the latitude from the JSON Data
#lat = data["coord"]["lat"]

# Pull the longitude from the JSON data
#lon = "" # Fix Me

#print("The latitude of {}: {}".format(cityName, lat))
#print("The longitude of {}: {}".format(cityName, lon))