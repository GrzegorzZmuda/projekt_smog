import json

import getwind


def winddata():
    a=getwind.weathernow()
    with open('wind.json', 'w') as json_file:
        json.dump(a, json_file)

    with open('wind.json','r') as json_file:
        a = json.load(json_file)
    return(a)


