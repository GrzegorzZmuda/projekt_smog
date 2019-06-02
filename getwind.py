import requests
import json


def weathernow():
    #Make a get request for Kraków weather.
    response = requests.get("http://api.openweathermap.org/data/2.5/weather?q=London&APPID=8fcc0c27bb02bace51a80ea5aae20fdd")
    #loadst content of response to object
    y = json.loads(response.content)
    if (len(y["wind"])<2):
        spd=0
        deg=0
    else:
        spd=y["wind"]["speed"]
        deg=y["wind"]["deg"]
    ret=[]
    ret.append(spd)
    ret.append(deg)

    return(ret)
weathernow()