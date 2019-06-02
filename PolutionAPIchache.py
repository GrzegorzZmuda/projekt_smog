import json
import PolutionAPI


def airdata():
    a=PolutionAPI.getSensors()
    with open('air.json', 'w') as json_file:
        json.dump(a, json_file)

    with open('air.json','r') as json_file:
        a = json.load(json_file)
    return(a)