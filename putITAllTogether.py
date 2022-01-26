import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
import time

#### First Script ##### 
cityName = "Boston"
appid = "" # Fix me
url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=imperial".format(cityName, appid)
resp = requests.get(url)
data = resp.json()
lat = data["coord"]["lat"]
lon = data["coord"]["lon"]
########################

##### Second Script ####
url2 = "https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&exclude=current,minutely,hourly,alerts&appid={}&units=imperial".format(lat, lon, appid)
resp2 = requests.get(url2)
data2 = resp2.json()
df = pd.DataFrame(data2)
df3 = pd.json_normalize(df["daily"])
df3["dt"] = pd.to_datetime(df3["dt"],unit='s')
df3["sunrise"] = pd.to_datetime(df3["sunrise"],unit='s')
df3["sunset"] = pd.to_datetime(df3["sunset"],unit='s')
df3["moonrise"] = pd.to_datetime(df3["moonrise"],unit='s')
df3["moonset"] = pd.to_datetime(df3["moonset"],unit='s')
df4 = df3[['dt', 'humidity', 'temp.day']]
########################

### Add Graph ##########
#define colors to use
col1 = 'blue'
col2 = 'red'
#define subplots
fig,ax = plt.subplots()
#add first line to plot
ax.plot(df4["dt"], df4["temp.day"], color=col1)
#add x-axis label
ax.set_xlabel('Date', fontsize=12)
#add y-axis label
ax.set_ylabel('Temp °F', color=col1, fontsize=12)
#define second y-axis that shares x-axis with current plot
ax2 = ax.twinx()
#add second line to plot
ax2.plot(df4["dt"], df4["humidity"], color=col2)
#add second y-axis label
ax2.set_ylabel('Humidity %', color=col2, fontsize=12)
#rotate plot ticks 45 degrees
ax.tick_params(labelrotation=45)
#Add Title
plt.title("5 Day Forcast")
#Add bottom margin to figure
fig.subplots_adjust(bottom=0.25)
#Show plot
plt.show()
########################