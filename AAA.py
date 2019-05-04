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

B:PolutionAPI.py pozwala na pobranie średniej temperatury, wilgotności, ciśnienia i poziomów PM z ostatniej godziny
b: Tutaj jest mapa czujników: https://airly.eu/map/pl/#50.07297,19.91483,i2935
b: Api zwraca przedział czasowy pomiarów, jest możliwość pobrania histori i prognozy

nie wiem jak z opadami ale na pewno brakuje godziny

//dla warunków bieżących dt Time of data calculation, unix, UTC
//dla prognozy list.dt_txt Data/time of calculation, UTC

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
 
 B: Stacje pomiarowe mierzą tylko pył zawieszony, chyba że znajdziecie jakiegoś innego dostawcę danych
 
 miejscami niebędącymi punktami pomiaru możemy się martwić później
 
 B: Api ma funkcję obliczania zanieczyszczeń w dowolnym miejscu, Wydaje mi się że liczy średnią z najbliższych sensorów

"""

