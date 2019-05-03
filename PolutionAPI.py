# -*- coding: utf-8 -*-
"""
Created on Fri May  3 12:53:48 2019

@author: Bartek



Api auth key: ZLhRWleBgEUhYxRaqg2rYhoOf3TKo45z
Request limits: 50/minute, 1000/day




"""

import requests
import json

testId = '2935'

#Odbierz dane z sensora o okreslonym id
def getSensorData(id):
    url="https://airapi.airly.eu/v2/measurements/installation?installationId="+id
    payload = {}
    headers = {'Accept': 'application/json', 'apikey': 'ZLhRWleBgEUhYxRaqg2rYhoOf3TKo45z'}

    r = requests.get(url, data=json.dumps(payload), headers=headers)
    
    if (r.status_code==200):#Sukcess?
        print(r.json().get("current").get("values")) #wypisz aktualne dane
    else:
        print("error")

#Odbierz informacje o sensorze o okreslonym id
def getSensorCord(id):   
    url="https://airapi.airly.eu/v2/installations/"+id
    payload = {}
    headers = {'Accept': 'application/json', 'apikey': 'ZLhRWleBgEUhYxRaqg2rYhoOf3TKo45z'}

    r = requests.get(url, data=json.dumps(payload), headers=headers)
    
    if (r.status_code==200):#Sukcess?
        print(r.json().get("location")) #wypisz aktualne dane
    else:
        print("error")
    
    
    
getSensorData(testId)
print("")
getSensorCord(testId)
"""
Możliwe zastosowania:
    -Lista pobliskich sensorów: /v2/installations/nearest 
    -dane z sensora: /v2/measurements/installation?installationId= (id)
    -lista instalacji: /v2/installations/
    -adres,współrzędne gps itp istalacji: /v2/installations/ (id)
"""
