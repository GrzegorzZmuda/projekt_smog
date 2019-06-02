import json
import time

import PolutionAPI


def airdata():
    tmp=time.time()

    with open('air.json','r') as json_file:
        a = json.load(json_file)


    if a[-1]-tmp>1800:
        a = PolutionAPI.getSensors()
        a.append(tmp)
        with open('air.json', 'w') as json_file:
            json.dump(a, json_file)

    with open('air.json','r') as json_file:
        a = json.load(json_file)
    return(a)


















