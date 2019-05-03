"""
Created on Fri May  3
@author: Grzegorz




downloadas current weather data from openweathermap.com
Don't use request too often - limited calls(60 per minute)
"""

import requests
import json

# Make a get request for Kraków weather.
response = requests.get("http://api.openweathermap.org/data/2.5/weather?q=Krakow&units=metric,pl&APPID=8fcc0c27bb02bace51a80ea5aae20fdd")
#loadst content of resonse to object
y = json.loads(response.content)

print(y)

"""
#prints data
print(y["coord"])
print(y["weather"])
print(y["main"])
print(y["wind"])
print(y["clouds"])
#print(y["dt"])
#print(y["sys"])
#print(y["id"])
#print(y["cod"])
#print(y["base"])

"""