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
    headers = {'Accept': 'application/json', 'apikey': 'hB2NtswdoFGIXd7FUUJ4mx8BNCvOSwsr'}

    r = requests.get(url, data=json.dumps(payload), headers=headers)

    if (r.status_code==200):#Sukcess?
        #print(r.json().get("current").get("values")[1]) #wypisz aktualne dane
        if (len(r.json().get("current").get("values"))>1):
            return(r.json().get("current").get("values")[1])

        else:

            x = '{ "name": "PM25", "value": 0}'
            y = json.loads(x)

            return(y)
    else:
        print("error")


#Odbierz informacje o sensorze o okreslonym id
def getSensorCord(id):   
    url="https://airapi.airly.eu/v2/installations/"+id
    payload = {}
    headers = {'Accept': 'application/json', 'apikey': 'hB2NtswdoFGIXd7FUUJ4mx8BNCvOSwsr'}

    r = requests.get(url, data=json.dumps(payload), headers=headers)
    
    if (r.status_code==200):#Sukcess?
        print(r.json().get("location")) #wypisz aktualne dane
    else:
        print("error")
#NIE UŻYWAC CZĘSTO, dużo requestów (20-30) max distance 5km (46)
#tworzy obiekt z informacją o lokacji czujnika i danymi o zanieczyszczeniu
def getSensors():
    url="https://airapi.airly.eu/v2/installations/nearest?lat=50.061389&lng=19.938333&maxDistanceKM=2&maxResults=20"
    payload = {}
    headers = {'Accept': 'application/json', 'apikey': 'hB2NtswdoFGIXd7FUUJ4mx8BNCvOSwsr'}

    r = requests.get(url, data=json.dumps(payload), headers=headers)

    if (r.status_code == 200):  # Sukcess?
        a=[]
        for i in range(len(r.json())):
            tmp1=r.json()[i]["id"],r.json()[i]["location"]
            tmp2=getSensorData(str(tmp1[0]))
            tmp=tmp1,tmp2
            a.append(tmp)

        return a
    else:
        print("error")
    

getSensors()
"""
Możliwe zastosowania:
    -Lista pobliskich sensorów: /v2/installations/nearest 
    -dane z sensora: /v2/measurements/installation?installationId= (id)
    -lista instalacji: /v2/installations/
    -adres,współrzędne gps itp istalacji: /v2/installations/ (id)
"""
