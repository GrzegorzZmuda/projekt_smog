# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 11:59:43 2019

@author: pichi
"""

import pickle

with open ('dane/analiza/godz2017.txt', 'rb') as fp:
    godz = pickle.load(fp)
    
with open ('dane/analiza/chmury2017.txt', 'rb') as fp: #chmury - segmenty po 20 punktów procentowych
    chmury = pickle.load(fp)
    
with open ('dane/analiza/opady2017.txt', 'rb') as fp:
    opady = pickle.load(fp)
    
with open ('dane/analiza/temp2017.txt', 'rb') as fp:
    temp = pickle.load(fp)
    
with open ('dane/analiza/wiatrkier2017.txt', 'rb') as fp:
    wiatrkier = pickle.load(fp)
    
with open ('dane/analiza/wiatrpr2017.txt', 'rb') as fp: #wiatrpr - segmenty po 5
    wiatrpr = pickle.load(fp)
    
with open ('dane/analiza/wilg2017.txt', 'rb') as fp:
    wilg = pickle.load(fp)
    
def znajdzwart(lista,x,stacja=0): #wynik: odchylenie stand., srednia]
    j=0
    for l in lista[2][0]:
        if (l==x):
            i=j
            break
    return lista[0][stacja][i], lista[1][stacja][i] 

    #[godzina,temperatura, wilgotnosc,zachmurzenie,deszcz(1=tak,0=nie),kierunek wiatru, prędkoć wiatru]

def znajdzwartosci(g,t,w,c,o,k,p,st=0):
    x=[]
    x.append( znajdzwart(godz,g,st) )
    x.append( znajdzwart(temp,t,st) )
    x.append( znajdzwart(wilg,w,st) )
    x.append( znajdzwart(chmury,c,st) )
    x.append( znajdzwart(opady,o,st) )
    x.append( znajdzwart(wiatrkier,k,st) )
    x.append( znajdzwart(wiatrpr,p,st) )
    
    sumasd=0
    
    for i in x:
        sumasd=sumasd+i[0]
    
    r=0
    for i in x:
        r=r+i[1]*(i[0]/sumasd)
        
    return r

print(znajdzwartosci(10,18,10,20,0,30,10,st=0))