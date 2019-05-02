# -*- coding: utf-8 -*-
"""
Created on Thu May  2 00:44:46 2019

@author: pi

https://docs.python-guide.org/scenarios/scrape/
"""

import requests
from bs4 import BeautifulSoup

page = requests.get('https://pogoda.interia.pl/archiwum-pogody-01-01-2019,cId,4970')

soup=BeautifulSoup(page.text,'html.parser')
temp = soup.find_all('span',attrs={'class': 'forecast-temp'})
hour=soup.find_all('span',attrs={'class': 'hour'})
minutes=soup.find_all('span',attrs={'class': 'minutes'})

w, h = 3,24;
res = [[0 for x in range(w)] for y in range(h)] 

i=0
for b in temp:
    res[i][2]=b.text
    i=i+1

    
i=0
for b in hour:
    res[i][0]=b.text
    i=i+1
    
i=0
for b in minutes:
    res[i][1]=b.text
    i=i+1

print(type(temp))
print(res)


