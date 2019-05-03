"""
Created on Fri May  3
@author: Grzegorz




downloadas forecast weather data from openweathermap.com
Don't use request too often - limited calls(60 per minute)
"""

import requests
import json

# Make a get request for Kraków weather.
response = requests.get("http://api.openweathermap.org/data/2.5/forecast/hourly?q=Krakow,pl&APPID=8fcc0c27bb02bace51a80ea5aae20fdd")
#loadst content of resonse to object
y = json.loads(response.content)
#prints forecast of wind
for i in range(96):
    z = y["list"][i]
    print(z["wind"])


#prints data
