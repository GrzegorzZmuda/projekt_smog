import json
import time

import PolutionAPI


def airdata():
    tmp=time.time()


    with open('air.json','r') as json_file:
        b = json.load(json_file)


    if tmp-b[-1]>1799:
        a = []
        a.append(PolutionAPI.getSensors())
        a.append(tmp)
        with open('air.json', 'w') as json_file:
            json.dump(a, json_file)
    else:
        a=b


    return(a[0])


















