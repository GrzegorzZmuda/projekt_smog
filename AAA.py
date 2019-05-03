# -*- coding: utf-8 -*-
"""
Created on Sat May  4 00:56:11 2019

@author: pi

JAK POBRAĆ DATĘ I GODZINĘ TYCH WSZYSTKICH DANYCH POWIEDZCIE MI....

Czynniki smogowe:
temperatura
wiatr - kierunek i siła
opady, prawdopodobnie
godzina
???cisnienie/wilgotnosc????? idk

nie wiem jak z opadami ale na pewno brakuje godziny

można pobrać ze stron dane temp i wiatru zależnie od godziny
 (będą takie same dla całego miasta raczej)
 i potem dla różnych punktów pomiaru smogu sprawdzić zależności
 temp mamy w komplecie z punktem pomiarowym więc tyle można prosto 

przewidywanie smogu -> branie najbardziej podobnych pomiarów
 dla danego punktu i wyliczanie średniej?? 
 to takie trochę brute force i by długo liczyło każde generowanie raczej
 albo generowanie jakiejs szalonej funkcji kilku zmiennych na podstawie starych danych
 
 Generalnie?? data i godzina ważne bardzo
 
 Czy patrzymy wgl tylko na pył zawieszony czy na jakies bardziej ambitne zwiazki siarki itd też??
 
 miejscami niebędącymi punktami pomiaru możemy się martwić później

"""

