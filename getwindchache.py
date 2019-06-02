import json
import datetime
import time

import getwind


def winddata():
    tmp=time.time()
    with open('wind.json','r') as json_file:
        a = json.load(json_file)
    if a[2]-tmp>1800:
        a=getwind.weathernow()
        a.append(tmp)
        with open('wind.json', 'w') as json_file:
             json.dump(a, json_file)

    with open('wind.json','r') as json_file:
        a = json.load(json_file)

    return(a)


