# -*- coding: utf-8 -*-
"""
Created on Thu May  2 00:44:46 2019

@author: pi

https://docs.python-guide.org/scenarios/scrape/
czytanie danych ze strony
"""

import requests
from bs4 import BeautifulSoup

def toint(txt):
    return int(''.join(filter(str.isdigit, txt)))

def pogoda(dzien,miesiac,rok): 
    #wynik: lista elementów [godzina,temperatura, wilgotnosc,zachmurzenie,deszcz(1=tak,0=nie)]
    adr="https://pogoda.interia.pl/archiwum-pogody-"+str(dzien)+"-"+str(miesiac)+"-"+str(rok)+",cId,4970"
    page = requests.get(adr)
    soup=BeautifulSoup(page.text,'html.parser')
    temp = soup.find_all('span',attrs={'class': 'forecast-temp'})
    hour=soup.find_all('span',attrs={'class': 'hour'})
    humidity=soup.find_all('div',attrs={'class': 'entry-humidity-wrap'})
    #class="entry-precipitation-value cloud-cover"
    clouds=soup.find_all('span',attrs={'class': 'entry-precipitation-value cloud-cover'})
    weather=soup.find_all('span',attrs={'class': 'forecast-phrase'})
    
    w, h = 5,24;
    res = [[0 for x in range(w)] for y in range(h)] 
    
    i=0
    for b in hour:
        res[i][0]=int(b.text)
        i=i+1
        
    
    i=0
    for b in temp:
        res[i][1]=toint(b.text)
        i=i+1
        
    i=0
    
    for b in humidity:
        res[i][2]=toint(b.text)
        i=i+1
        
    i=0
    
    for b in clouds:
        res[i][3]=toint(b.text)
        i=i+1
        
    i=0
    
    for b in weather:
        if "Deszcz" in b.text or "deszcz" in b.text or "opad" in b.text or "Opad" in b.text:
            res[i][4]=1
        i=i+1
    
        
    print(type(temp))
    print(res)
    return res

pog=pogoda("01","01",2019)


