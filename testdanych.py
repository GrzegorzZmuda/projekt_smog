# -*- coding: utf-8 -*-
"""
Created on Sun May 12 19:02:12 2019

@author: pichi
"""

import stacje, pogoda

#temperatura: -35 do 40

temp=[]
p=[]
o=0


def pogodaH(dzien,miesiac,rok,godzina):
    #wynik: [godzina,temperatura, wilgotnosc,zachmurzenie,deszcz(1=tak,0=nie)]
    res= pogoda.pogodaD(dzien,miesiac,rok)
    return res[godzina]

def podziel(lista,minimum,param):
    res=[]
    for i in lista:
        res[i[param]-minimum].append(i)
    
    return res

testowalista=[]
for i in range (5):
    testowalista.append(pm10_2017[0][i])

i=0
j=0
while i < (len(p2017)):
    p.append(pogodaD(p2017[i].day,p2017[i].month,p2017[i].year))
    print(i/24)
    i=i+24


#zapisz listę p do pliku
#with open('dane/pogoda2017.txt', 'wb') as fp:
#    pickle.dump(p, fp)

